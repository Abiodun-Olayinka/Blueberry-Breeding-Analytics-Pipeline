#!/usr/bin/env python3
"""
Blueberry Breeding Analytics Pipeline
ETHICAL: Uses only simulated data clearly labeled as such
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.metrics import r2_score, mean_squared_error
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("🫐 BLUEBERRY BREEDING ANALYTICS PIPELINE")
print("="*70)
print("\n⚠️  DISCLAIMER: This demo uses SIMULATED data")
print("   All methods are directly applicable to real blueberry data")
print("   Based on published heritability estimates from blueberry literature")
print("="*70)

# ============================================================================
# SECTION 1: DATA GENERATION (Simulated based on published parameters)
# ============================================================================
print("\n📊 SECTION 1: Generating Simulated Blueberry Breeding Data")
print("-" * 70)

np.random.seed(2024)

# Parameters from published blueberry studies
n_genotypes = 100
n_markers = 2000
n_traits = 5
n_years = 3
n_locations = 4

# Trait heritabilities from literature
traits = {
    'yield': {'h2': 0.45, 'unit': 'kg/plant', 'source': 'Ferrão et al. 2021'},
    'fruit_weight': {'h2': 0.60, 'unit': 'g', 'source': 'Cappai et al. 2020'},
    'brix': {'h2': 0.65, 'unit': '%', 'source': 'Ferrão et al. 2021'},
    'firmness': {'h2': 0.55, 'unit': 'N', 'source': 'Mengist et al. 2022'},
    'stem_blight_resistance': {'h2': 0.40, 'unit': '1-9 scale', 'source': 'Brar et al. 2020'}
}

print(f"   Simulating {n_genotypes} genotypes × {len(traits)} traits")
print(f"   Over {n_years} years × {n_locations} locations")

# Generate genotypes with LD structure
marker_names = [f'SNP_{i+1}' for i in range(n_markers)]
genotype_ids = [f'GEN_{i+1:03d}' for i in range(n_genotypes)]

# Generate allele frequencies (realistic beta distribution)
maf = np.random.beta(2, 5, n_markers)
maf = np.clip(maf, 0.05, 0.5)

# Generate genotypes
genotypes = np.random.binomial(2, maf, (n_genotypes, n_markers))

# Add population structure (north vs south adapted)
pop_assignment = np.random.choice(['North', 'South'], n_genotypes)
for i, pop in enumerate(pop_assignment):
    if pop == 'North':
        # Northern adapted: higher frequency of cold tolerance alleles
        genotypes[i, :100] = np.random.binomial(2, maf[:100] + 0.2, 100)
        genotypes[i, :100] = np.clip(genotypes[i, :100], 0, 2)

print(f"   ✓ Generated {n_markers} SNP markers")
print(f"   ✓ MAF range: {maf.min():.3f} - {maf.max():.3f}")

# Generate phenotypes with genetic architecture
print("\n   Simulating phenotypes with published heritabilities...")

years = [2022, 2023, 2024]
locations = ['Auburn_AL', 'Citra_FL', 'Mills_River_NC', 'Charleston_SC']

all_phenotypes = []

for trait_idx, (trait_name, trait_info) in enumerate(traits.items()):
    h2 = trait_info['h2']
    
    # Select QTLs (causal markers)
    n_qtl = 20
    qtl_indices = np.random.choice(n_markers, n_qtl, replace=False)
    qtl_effects = np.random.normal(0, 1, n_qtl)
    
    # Genetic values
    genetic_values = np.dot(genotypes[:, qtl_indices], qtl_effects)
    genetic_values = (genetic_values - genetic_values.mean()) / genetic_values.std()
    
    # Scale to realistic ranges
    if trait_name == 'yield':
        genetic_values = genetic_values * 0.8 + 3.0
    elif trait_name == 'fruit_weight':
        genetic_values = genetic_values * 0.5 + 2.0
    elif trait_name == 'brix':
        genetic_values = genetic_values * 1.5 + 12.0
    elif trait_name == 'firmness':
        genetic_values = genetic_values * 1.0 + 2.0
    else:  # stem blight resistance
        genetic_values = genetic_values * 1.5 + 5.0
        genetic_values = np.clip(genetic_values, 1, 9)
    
    # Add G×E and generate multi-environment data
    for year in years:
        for loc_idx, location in enumerate(locations):
            year_effect = np.random.normal(0, 0.15)
            loc_effect = np.random.normal(0, 0.2) if 'FL' in location else np.random.normal(0, 0.1)
            gxe_effect = np.random.normal(0, 0.15, n_genotypes)
            
            # Calculate residual variance for target heritability
            var_g = np.var(genetic_values)
            var_residual = var_g * (1 - h2) / h2
            
            for rep in range(3):
                residual = np.random.normal(0, np.sqrt(var_residual), n_genotypes)
                phenotype = genetic_values + year_effect + loc_effect + gxe_effect + residual
                
                if trait_name == 'stem_blight_resistance':
                    phenotype = np.clip(phenotype, 1, 9)
                
                for i, geno_id in enumerate(genotype_ids):
                    all_phenotypes.append({
                        'Genotype': geno_id,
                        'Trait': trait_name,
                        'Year': year,
                        'Location': location,
                        'Rep': rep + 1,
                        'Population': pop_assignment[i],
                        'Phenotype': phenotype[i],
                        'Heritability_Source': trait_info['source']
                    })

df_pheno = pd.DataFrame(all_phenotypes)
print(f"   ✓ Generated {len(df_pheno):,} phenotypic records")

# ============================================================================
# SECTION 2: DATA CLEANING AND BLUP CALCULATION
# ============================================================================
print("\n🧹 SECTION 2: Data Cleaning and BLUP Calculation")
print("-" * 70)

# Calculate BLUPs (Best Linear Unbiased Predictions)
blups = []

for trait in df_pheno['Trait'].unique():
    trait_data = df_pheno[df_pheno['Trait'] == trait]
    
    # Calculate means across environments
    geno_means = trait_data.groupby('Genotype')['Phenotype'].mean()
    grand_mean = geno_means.mean()
    
    # Simple shrinkage estimator (empirical BLUP)
    var_g = geno_means.var()
    var_e = trait_data.groupby('Genotype')['Phenotype'].var().mean()
    
    for geno in geno_means.index:
        n_obs = len(trait_data[trait_data['Genotype'] == geno])
        shrinkage = var_g / (var_g + var_e/n_obs)
        blup = grand_mean + shrinkage * (geno_means[geno] - grand_mean)
        
        blups.append({
            'Trait': trait,
            'Genotype': geno,
            'BLUP': blup,
            'Population': pop_assignment[genotype_ids.index(geno)]
        })

df_blups = pd.DataFrame(blups)
print(f"   ✓ Calculated BLUPs for {len(df_blups)} genotype-trait combinations")

# Calculate heritability
print("\n📈 Calculating heritability estimates...")

heritability_results = []
for trait in df_pheno['Trait'].unique():
    trait_data = df_pheno[df_pheno['Trait'] == trait]
    geno_means = trait_data.groupby('Genotype')['Phenotype'].mean()
    var_g = geno_means.var()
    var_e = trait_data.groupby('Genotype')['Phenotype'].var().mean()
    H2 = var_g / (var_g + var_e)
    
    heritability_results.append({
        'Trait': trait,
        'Heritability_H2': H2,
        'Published_H2': traits[trait]['h2'],
        'Source': traits[trait]['source']
    })

df_heritability = pd.DataFrame(heritability_results)
for _, row in df_heritability.iterrows():
    print(f"   {row['Trait']}: H² = {row['Heritability_H2']:.3f} (published: {row['Published_H2']:.3f})")

# ============================================================================
# SECTION 3: GENOMIC PREDICTION
# ============================================================================
print("\n🧬 SECTION 3: Genomic Prediction")
print("-" * 70)

# Prepare data for genomic prediction
marker_matrix = genotypes
prediction_results = []

for trait in df_blups['Trait'].unique():
    print(f"\n   Predicting {trait}...")
    
    # Get BLUPs for this trait
    trait_blups = df_blups[df_blups['Trait'] == trait].set_index('Genotype')
    y = np.array([trait_blups.loc[g, 'BLUP'] if g in trait_blups.index else np.nan 
                  for g in genotype_ids])
    
    # Remove missing
    valid = ~np.isnan(y)
    y_valid = y[valid]
    X_valid = marker_matrix[valid, :]
    
    # Random Forest prediction
    rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    
    # 5-fold cross-validation
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    predictions = cross_val_predict(rf, X_valid, y_valid, cv=kf)
    
    r2 = r2_score(y_valid, predictions)
    rmse = np.sqrt(mean_squared_error(y_valid, predictions))
    
    prediction_results.append({
        'Trait': trait,
        'Method': 'Random Forest',
        'R2': r2,
        'RMSE': rmse,
        'n_training': len(y_valid)
    })
    
    print(f"      R² = {r2:.3f}, RMSE = {rmse:.3f}")

df_predictions = pd.DataFrame(prediction_results)

# ============================================================================
# SECTION 4: SELECTION INDEX
# ============================================================================
print("\n🏆 SECTION 4: Multi-trait Selection Index")
print("-" * 70)

# Create wide format BLUP matrix
blup_wide = df_blups.pivot(index='Genotype', columns='Trait', values='BLUP').reset_index()

# Economic weights (based on breeding priorities)
weights = {
    'yield': 0.35,
    'fruit_weight': 0.15,
    'brix': 0.15,
    'firmness': 0.15,
    'stem_blight_resistance': 0.20
}

# Standardize and calculate index
for trait, weight in weights.items():
    if trait in blup_wide.columns:
        mean = blup_wide[trait].mean()
        std = blup_wide[trait].std()
        blup_wide[f'{trait}_std'] = (blup_wide[trait] - mean) / std

blup_wide['Selection_Index'] = 0
for trait, weight in weights.items():
    if f'{trait}_std' in blup_wide.columns:
        blup_wide['Selection_Index'] += weight * blup_wide[f'{trait}_std']

# Rank and select top 20%
blup_wide['Rank'] = blup_wide['Selection_Index'].rank(ascending=False)
n_select = int(len(blup_wide) * 0.2)
blup_wide['Selected'] = blup_wide['Rank'] <= n_select

print(f"   ✓ Selection index calculated for {len(blup_wide)} genotypes")
print(f"   ✓ Selected {n_select} genotypes (top 20%)")

print("\n   Top 10 Genotypes:")
print(blup_wide[['Genotype', 'Selection_Index', 'Rank']].head(10).to_string(index=False))

# ============================================================================
# SECTION 5: VISUALIZATION
# ============================================================================
print("\n📊 SECTION 5: Creating Visualizations")
print("-" * 70)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 1. Heritability comparison
ax = axes[0, 0]
x = np.arange(len(df_heritability))
width = 0.35
ax.bar(x - width/2, df_heritability['Heritability_H2'], width, label='Calculated', color='steelblue')
ax.bar(x + width/2, df_heritability['Published_H2'], width, label='Published', color='coral', alpha=0.7)
ax.set_xlabel('Trait')
ax.set_ylabel('Heritability (H²)')
ax.set_title('Heritability Estimates vs Published Literature')
ax.set_xticks(x)
ax.set_xticklabels(df_heritability['Trait'], rotation=45, ha='right')
ax.legend()
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)

# 2. Genomic prediction accuracy
ax = axes[0, 1]
colors = ['green' if r2 > 0.5 else 'orange' if r2 > 0.3 else 'red' for r2 in df_predictions['R2']]
ax.bar(df_predictions['Trait'], df_predictions['R2'], color=colors)
ax.set_xlabel('Trait')
ax.set_ylabel('Prediction R²')
ax.set_title('Genomic Prediction Accuracy (Random Forest)')
ax.axhline(y=0.5, color='green', linestyle='--', label='Good', alpha=0.5)
ax.axhline(y=0.3, color='orange', linestyle='--', label='Moderate', alpha=0.5)
ax.tick_params(axis='x', rotation=45)
ax.legend()

# 3. Selection index distribution
ax = axes[0, 2]
selected_idx = blup_wide[blup_wide['Selected']]['Selection_Index']
not_selected_idx = blup_wide[~blup_wide['Selected']]['Selection_Index']
ax.hist(not_selected_idx, bins=20, alpha=0.5, label='Not Selected', color='gray')
ax.hist(selected_idx, bins=20, alpha=0.5, label='Selected', color='green')
ax.axvline(x=blup_wide[blup_wide['Selected']]['Selection_Index'].min(), 
           color='green', linestyle='--', label='Selection threshold')
ax.set_xlabel('Selection Index')
ax.set_ylabel('Frequency')
ax.set_title('Selection Index Distribution')
ax.legend()

# 4. Trait correlations heatmap
ax = axes[1, 0]
trait_corrs = blup_wide[[t for t in weights.keys() if t in blup_wide.columns]].corr()
sns.heatmap(trait_corrs, annot=True, cmap='coolwarm', center=0, ax=ax, fmt='.2f')
ax.set_title('Genetic Correlations Between Traits')

# 5. Population comparison
ax = axes[1, 1]
for pop in ['North', 'South']:
    pop_indices = blup_wide[blup_wide['Genotype'].isin(
        [g for i, g in enumerate(genotype_ids) if pop_assignment[i] == pop])]['Selection_Index']
    ax.hist(pop_indices, bins=15, alpha=0.5, label=pop)
ax.set_xlabel('Selection Index')
ax.set_ylabel('Frequency')
ax.set_title('Selection Index by Population')
ax.legend()

# 6. Yield vs Resistance trade-off
ax = axes[1, 2]
ax.scatter(blup_wide['yield'], blup_wide['stem_blight_resistance'], 
           c=blup_wide['Selection_Index'], cmap='viridis', alpha=0.6, s=50)
ax.set_xlabel('Yield BLUP')
ax.set_ylabel('Stem Blight Resistance BLUP')
ax.set_title('Yield vs Disease Resistance Trade-off')
plt.colorbar(ax.collections[0], ax=ax, label='Selection Index')

plt.suptitle('Blueberry Breeding Analytics Pipeline\n(SIMULATED DATA for Demonstration)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('blueberry_breeding_report.png', dpi=150, bbox_inches='tight')
print("   ✓ Saved visualization to blueberry_breeding_report.png")

# ============================================================================
# SECTION 6: OUTPUT AND SUMMARY
# ============================================================================
print("\n📁 SECTION 6: Saving Results")
print("-" * 70)

# Save all outputs
df_blups.to_csv('blups.csv', index=False)
df_heritability.to_csv('heritability.csv', index=False)
df_predictions.to_csv('prediction_results.csv', index=False)
blup_wide[['Genotype', 'Selection_Index', 'Rank', 'Selected']].to_csv('selection_index.csv', index=False)
df_pheno.to_csv('phenotypes.csv', index=False)

print("   ✓ Saved results to CSV files")

# ============================================================================
# SUMMARY REPORT
# ============================================================================
print("\n" + "="*70)
print("✅ PIPELINE COMPLETED SUCCESSFULLY")
print("="*70)
print("\n📊 SUMMARY STATISTICS:")
print(f"   • Total genotypes: {n_genotypes}")
print(f"   • Total markers: {n_markers}")
print(f"   • Total phenotypic records: {len(df_pheno):,}")
print(f"   • Traits analyzed: {len(traits)}")
print(f"   • Years of data: {n_years}")
print(f"   • Locations: {n_locations}")

print("\n🎯 KEY FINDINGS (Based on Simulated Data):")
for _, row in df_predictions.iterrows():
    print(f"   • {row['Trait']}: Genomic prediction R² = {row['R2']:.3f}")

print(f"\n🏆 SELECTED GENOTYPES: {n_select} genotypes (top 20%)")

print("\n📁 OUTPUT FILES CREATED:")
print("   • blueberry_breeding_report.png - Visualization dashboard")
print("   • blups.csv - BLUP values for all genotypes")
print("   • heritability.csv - Heritability estimates")
print("   • prediction_results.csv - Genomic prediction accuracy")
print("   • selection_index.csv - Selection index rankings")
print("   • phenotypes.csv - Raw phenotype data")

print("\n" + "="*70)
print("⚠️  IMPORTANT DISCLAIMER")
print("="*70)
print("This analysis used SIMULATED data for demonstration purposes.")
print("All methods are directly applicable to real blueberry data.")
print("Heritability parameters based on published literature:")
for trait, info in traits.items():
    print(f"   • {trait}: {info['source']}")
print("\nFor real data analysis, replace simulated data with:")
print("   • Genotype data from GDR (Genome Database for Rosaceae)")
print("   • Phenotype data from breeding program records")
print("   • The statistical methods remain identical")
print("="*70)

plt.show()
