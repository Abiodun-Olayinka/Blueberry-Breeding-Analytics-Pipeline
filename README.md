# 🫐 Blueberry Breeding Analytics Pipeline

**A comprehensive computational pipeline for small fruit breeding programs** implementing genomic prediction, BLUP calculation, heritability estimation and multi-trait selection indices.

![Blueberry Breeding Report](https://raw.githubusercontent.com/Abiodun-Olayinka/blueberry-breeding-pipeline/main/blueberry_breeding_report.png)

---

## Why This Pipeline?

Plant breeding programs generate large amounts of phenotypic and genomic data, but turning that data into **productive selection decisions** remains a major challenge.

**Blueberry Breeding Analytics Pipeline** was built to solve this by providing a complete, easy-to-use workflow that combines:

- Accurate statistical genetics (BLUPs & heritability)
- Modern genomic prediction using Random Forest
- Smart multi-trait selection indices with economic weights
- Professional visualization dashboard

**Perfect for:**
- Blueberry and small fruit breeders
- Graduate students and researchers in plant breeding & genetics
- Breeding programs with limited bioinformatics support
- Anyone seeking reproducible, literature-validated breeding analytics

Instead of spending weeks writing custom scripts, you can run a full breeding cycle analysis in minutes — with results that match published scientific literature.

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
- [Acknowledgments](#acknowledgments)

---

## 📊 Overview
This pipeline implements state-of-the-art statistical genetics methods tailored for **blueberry** (*Vaccinium* spp.) and other small fruit breeding programs. It integrates realistic data simulation, BLUPs, genomic prediction and selection indices into one seamless workflow.

---

## ✨ Features

| Category              | Features |
|-----------------------|----------|
| Data Simulation       | Realistic SNP data with LD structure, G×E interactions and population structure |
| Statistical Genetics  | BLUP calculation, broad-sense heritability (H²), variance components |
| Genomic Prediction    | Random Forest regression, 5-fold cross-validation, R² and RMSE metrics |
| Selection Index       | Multi-trait selection with customizable economic weights and genotype ranking |
| Visualization         | Professional 6-panel dashboard (heritability, accuracy, correlations, trade-offs) |

---

## 🚀 Quick Start

**Prerequisites**  
- Python 3.8 or higher

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

| File                          | Description                                      |
|-------------------------------|--------------------------------------------------|
| `blueberry_breeding_report.png` | Complete 6-panel visualization dashboard       |
| `blups.csv`                   | Best Linear Unbiased Predictions (BLUPs)         |
| `heritability.csv`            | Heritability estimates by trait                  |
| `prediction_results.csv`      | Genomic prediction accuracy metrics              |
| `selection_index.csv`         | Final genotype rankings                          |
| `phenotypes.csv`              | Simulated raw phenotypic data                    |

---

## 📈 Example Results

### Heritability Estimates

| Trait                  | This Pipeline | Published Range   | Source |
|------------------------|---------------|-------------------|--------|
| Yield                  | 0.450         | 0.35–0.65         | Cellon et al. (2018); Ferrão et al. (2018) |
| Brix (Soluble Solids)  | 0.651         | 0.60–0.80         | Ferrão et al. (2018); Babiker et al. (2025) |
| Firmness               | 0.542         | 0.45–0.70         | Liu et al. (2020); Cappai et al. (2018) |
| Fruit Weight           | 0.516         | 0.20–0.90         | Mengist et al. (2020) |
| Glucose/Fructose       | 0.80–0.83     | 0.75–0.85         | Chen et al. (2025) |

### Genomic Prediction Accuracy (Random Forest)

| Trait       | R²    | RMSE   |
|-------------|-------|--------|
| Yield       | 0.10  | 0.77   |
| Brix        | 0.24  | 1.31   |
| Firmness    | 0.39  | 0.77   |

---

## 🧬 Methods

- **BLUP Calculation** — Best Linear Unbiased Prediction using shrinkage estimation across environments.  
- **Heritability Estimation** — Broad-sense heritability (**H²**) calculated as the ratio of genetic to phenotypic variance components.  
- **Genomic Prediction** — Random Forest regression (100 trees, max depth 10) with 5-fold cross-validation.  
- **Selection Index** — Multi-trait selection index with standardized traits and user-defined economic weights.

---

## 📚 Literature Cited

### Heritability Sources Summary

| Trait                  | This Pipeline | Published Range   | Source |
|------------------------|---------------|-------------------|--------|
| Yield                  | 0.450         | 0.35–0.65         | Cellon et al. (2018); Ferrão et al. (2018) |
| Brix (Soluble Solids)  | 0.651         | 0.60–0.80         | Ferrão et al. (2018); Babiker et al. (2025) |
| Firmness               | 0.542         | 0.45–0.70         | Liu et al. (2020); Cappai et al. (2018) |
| Fruit Weight           | 0.516         | 0.20–0.90         | Mengist et al. (2020) |
| Glucose/Fructose       | 0.80–0.83     | 0.75–0.85         | Chen et al. (2025) |

### Complete References

- **Cellon, C., et al.** (2018). Estimation of genetic parameters and prediction of breeding values in an autotetraploid blueberry breeding population with extensive pedigree data. *Euphytica*, 214, 87. https://doi.org/10.1007/s10681-018-2165-8

- **Ferrão, L. F. V., et al.** (2018). Insights into the genetic basis of blueberry fruit-related traits using diploid and tetraploid models. *Frontiers in Ecology and Evolution*, 6, 107. https://doi.org/10.3389/fevo.2018.00107

- **Mengist, M. F., et al.** (2020). Diversity in metabolites and fruit quality traits in blueberry enables ploidy and species differentiation and establishes a strategy for future genetic studies. *Frontiers in Plant Science*, 11, 592222. https://doi.org/10.3389/fpls.2020.592222

- **Babiker, E., et al.** (2025). Phenological variation associates with the stability of fruit quality traits in cultivated tetraploid blueberry. *G3: Genes, Genomes, Genetics*, 15(7), jkaf108. https://doi.org/10.1093/g3journal/jkaf108

- **Liu, Y. C., et al.** (2020). Screening and inheritance of fruit storage-related traits based on reciprocal cross of southern × northern high bush blueberry. *Scientia Agricultura Sinica*, 53(19), 4045–4055.

- **Chen, L., et al.** (2025). Inheritance analysis of sugar and organic acid components in blueberry hybrid progenies. *Scientia Horticulturae*, 350, 113789. https://doi.org/10.1016/j.scienta.2025.113789

- **Cappai, F., et al.** (2018). Molecular and genetic bases of fruit firmness variation in blueberry—A review. *Agronomy*, 8(9), 174. https://doi.org/10.3390/agronomy8090174

---

## 🔧 Customization

Edit **`config.yaml`** for easy parameter adjustment (number of genotypes, SNPs, trait weights, etc.).

```yaml
trait_weights:
  yield: 0.35
  fruit_weight: 0.15
  brix: 0.15
  firmness: 0.15
  stem_blight_resistance: 0.20
```

---

## 📚 Citation

```bibtex
@software{blueberry_breeding_pipeline,
  author = {Olayinka, Abiodun},
  title = {Blueberry Breeding Analytics Pipeline},
  year = {2026},
  url = {https://github.com/Abiodun-Olayinka/blueberry-breeding-pipeline}
}
```

---

## 📄 License
**MIT License** — See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

This pipeline builds upon the foundational work of the blueberry genetics community:

- Cellon et al. (2018) — Genetic parameters in tetraploid blueberry  
- Ferrão et al. (2018) — Genetic architecture of fruit traits  
- Mengist et al. (2020), Babiker et al. (2025), Liu et al. (2020), Chen et al. (2025), and Cappai et al. (2018)

<div align="center">
  <strong>Made with ❤️ for the plant breeding community</strong>
</div>
