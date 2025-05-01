# 🖼️ Logo Similarity Project

**Logo Similarity** project — an initiative to intelligently group websites based on the visual similarity of their logos.
No heavyweight ML clustering (like K-Means or DBSCAN) — just efficient perceptual image analysis and hashing.

---

## 🚀 Project Overview

Logos are a company's visual fingerprint. This project focuses on:

- **Extracting** logos from a given dataset
- **Processing** and **normalizing** the images
- **Comparing** logos to detect visual similarity
- **Grouping** similar websites together based on their brand visuals

The challenge?
Making it work **accurately** without relying on classic machine learning clustering methods.

---


## 🧠 How It Works

1. **Logo Extraction** — Favicon URLs are inferred from domains and downloaded automatically
2. **Image Hashing** — Logos are processed (grayscale + resized) and hashed using perceptual hashing (`phash`)
3. **Similarity Grouping** — Logo hashes are compared using Hamming distance and grouped if below a similarity threshold

---

## ⚒️ Project Structure

```
logo-similarity/
├── batch/         # Quick scripts for setup and running
├── data/          # Input data (logos.snappy.parquet, images)
├── output/        # Grouped results
├── logosim/       # Source code (main logic modules)
├── tests/         # Automated tests (optional)
├── README.md      # This file
├── requirements.txt
└── .gitignore
```

---

## 🚧 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Fillinlak3/logo-similarity.git
   cd logo-similarity
   ```

2. Create & activate a virtual environment:
   ```bash
   python -m venv logosim_env
   .\logosim_env\Scripts\activate    # Windows
   source logosim_env/bin/activate    # Mac/Linux
   ```
   Or use `batch/activate_venv.bat` for quick execution.

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or use `batch/install_requirements.bat` for quick execution.

4. Run the project:
   ```bash
   py -3.10 logosim/main.py
   ```
   Or use `batch/run_project.bat` for quick execution.

---

## 📦 Dependencies

- Python 3.10
- pandas
- pyarrow
- requests
- opencv-python
- imagehash
- Pillow
- scikit-learn
- tqdm

---

## 📄 Status

- [x] Project structure & setup
- [x] Virtual environment and scripts
- [x] Dataset ready to load
- [x] Image processing & similarity logic
- [x] Final grouping output (into _output/groups.json_)

---

## 📊 Example Output (groups.json)

```json
[
  ["nike.com.png", "nikestore.co.uk.png"],
  ["cocacola.com.png"],
  ["apple.com.png", "apple-inc.net.png", "macstore.org.png"]
]
```

---

## 📃 License

This project is developed for educational purposes as part of the Veridion Internship Challenge.
