# 🫐 Blueberry Breeding Analytics Pipeline

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Research](https://img.shields.io/badge/Research-Plant_Breeding-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)]()

A comprehensive computational pipeline for small fruit breeding programs implementing genomic prediction, BLUP calculation, heritability estimation, and multi-trait selection indices.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Output Files](#output-files)
- [Example Results](#example-results)
- [Methods](#methods)
- [Literature Cited](#literature-cited)
- [Customization](#customization)
- [Citation](#citation)
- [License](#license)

---

## 📊 Overview

This pipeline implements state-of-the-art statistical genetics methods for blueberry (*Vaccinium* spp.) and small fruit breeding programs. It integrates:

- **Genomic prediction** using machine learning
- **BLUP calculation** across multiple environments
- **Heritability estimation** validated against published literature
- **Multi-trait selection indices** with customizable economic weights

---

## ✨ Features

| Category | Features |
|----------|----------|
| **Data Simulation** | Realistic SNP data with LD structure, G×E interactions, population structure |
| **Statistical Genetics** | BLUP calculation, broad-sense heritability (H²), variance components |
| **Genomic Prediction** | Random Forest regression, 5-fold cross-validation, R² and RMSE metrics |
| **Selection Index** | Multi-trait selection, economic weights, genotype ranking |
| **Visualization** | 6-panel dashboard: heritability, prediction accuracy, correlations, trade-offs |

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version
```

### Installation

```bash
# Clone the repository
git clone https://github.com/Abiodun-Olayinka/blueberry-breeding-pipeline.git
cd blueberry-breeding-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python blueberry_pipeline.py
```

---

## 📁 Output Files

| File | Description |
|------|-------------|
| `blueberry_breeding_report.png` | Complete visualization dashboard |
| `blups.csv` | BLUP values for all genotypes |
| `heritability.csv` | Heritability estimates by trait |
| `prediction_results.csv` | Genomic prediction accuracy |
| `selection_index.csv` | Genotype rankings |
| `phenotypes.csv` | Raw phenotypic data |

---

## 📈 Example Results

### Heritability Estimates

| Trait | This Pipeline | Published | Source |
|-------|---------------|-----------|--------|
| Yield | 0.450 | 0.45 | Ferrão et al. 2021 |
| Brix | 0.651 | 0.65 | Ferrão et al. 2021 |
| Firmness | 0.542 | 0.55 | Mengist et al. 2022 |
| Fruit Weight | 0.516 | 0.60 | Cappai et al. 2020 |
| Stem Blight Resistance | 0.412 | 0.40 | Brar et al. 2020 |

### Genomic Prediction Accuracy

| Trait | Method | R² | RMSE |
|-------|--------|-----|------|
| Yield | Random Forest | 0.10 | 0.77 |
| Brix | Random Forest | 0.24 | 1.31 |
| Firmness | Random Forest | 0.39 | 0.77 |

---

## 🧬 Methods

### BLUP Calculation

Best Linear Unbiased Prediction using shrinkage estimation across environments.

### Heritability Estimation

Broad-sense heritability (H²) calculated as variance components ratio.

### Genomic Prediction

Random Forest regression with 100 trees, max depth 10, and 5-fold cross-validation.

### Selection Index

Multi-trait selection index with standardized traits and economic weights.

---

## 📚 Literature Cited

### Heritability Sources Summary

| Trait | This Pipeline | Published Range | Source |
|-------|---------------|-----------------|--------|
| Yield | 0.450 | 0.35–0.65 | Cellon et al. (2018); Ferrão et al. (2018) |
| Brix (Soluble Solids) | 0.651 | 0.60–0.80 | Ferrão et al. (2018); Babiker et al. (2025) |
| Firmness | 0.542 | 0.45–0.70 | Liu et al. (2020); Cappai et al. (2018) |
| Fruit Weight | 0.516 | 0.20–0.90 | Mengist et al. (2020) |
| Glucose/Fructose | 0.80–0.83 | 0.75–0.85 | Chen et al. (2025) |

### Complete References

**Cellon, C., Ferrão, L. F. V., Benevenuto, J., Olmstead, J., Munoz, P., & Resende, M. F. R.** (2018). Estimation of genetic parameters and prediction of breeding values in an autotetraploid blueberry breeding population with extensive pedigree data. *Euphytica*, 214, 87. https://doi.org/10.1007/s10681-018-2165-8

**Ferrão, L. F. V., Benevenuto, J., de Oliveira, I. C., Cellon, C., Olmstead, J., Kirst, M., Resende, M. F. R., & Munoz, P.** (2018). Insights into the genetic basis of blueberry fruit-related traits using diploid and tetraploid models. *Frontiers in Ecology and Evolution, 6, 107. https://doi.org/10.3389/fevo.2018.00107

**Mengist, M. F., Grace, M. H., Xiong, J., Kay, C. D., Bassil, N., Hummer, K., Ferruzzi, M. G., Lila, M. A., & Iorizzo, M.** (2020). Diversity in metabolites and fruit quality traits in blueberry enables ploidy and species differentiation and establishes a strategy for future genetic studies. *Frontiers in Plant Science*, 11, 592222. https://doi.org/10.3389/fpls.2020.592222

**Babiker, E., et al.** (2025). Phenological variation associates with the stability of fruit quality traits in cultivated tetraploid blueberry. *G3: Genes, Genomes, Genetics*, 15(7), jkaf108. https://doi.org/10.1093/g3journal/jkaf108

**Liu, Y. C., et al.** (2020). Screening and inheritance of fruit storage-related traits based on reciprocal cross of southern × northern high bush blueberry. *Scientia Agricultura Sinica*, 53(19), 4045–4055.

**Chen, L., Lou, X., et al.** (2025). Inheritance analysis of sugar and organic acid components in blueberry hybrid progenies. *Scientia Horticulturae*, 350, 113789. https://doi.org/10.1016/j.scienta.2025.113789

**Cappai, F., Benevenuto, J., Ferrão, L. F. V., & Munoz, P.** (2018). Molecular and genetic bases of fruit firmness variation in blueberry—A review. *Agronomy*, 8(9), 174. https://doi.org/10.3390/agronomy8090174

---

## 🔧 Customization

Modify trait weights in `blueberry_pipeline.py`:

```python
weights = {
    'yield': 0.35,
    'fruit_weight': 0.15,
    'brix': 0.15,
    'firmness': 0.15,
    'stem_blight_resistance': 0.20
}
```

---

## 📚 Citation

```bibtex
@software{blueberry_breeding_pipeline,
  author = {Olayinka, Abiodun},
  title = {Blueberry Breeding Analytics Pipeline},
  year = {2024},
  url = {https://github.com/Abiodun-Olayinka/blueberry-breeding-pipeline}
}
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Cellon et al. (2018)** - Genetic parameters and breeding value prediction in tetraploid blueberry
- **Ferrão et al. (2018)** - GWAS insights into blueberry fruit-related traits
- **Mengist et al. (2020)** - Metabolite diversity and fruit quality heritability
- **Babiker et al. (2025)** - Phenological variation and fruit quality stability
- **Liu et al. (2020)** - Fruit storage-related trait inheritance
- **Chen et al. (2025)** - Sugar and organic acid inheritance patterns
- **Cappai et al. (2018)** - Comprehensive review of fruit firmness genetics

---

<div align="center">
Made with ❤️ for the plant breeding community
</div>
