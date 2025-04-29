# 🖼️ Logo Similarity Project

Welcome to the **Logo Similarity** project — an initiative to intelligently group websites based on the visual similarity of their logos.
No heavy clustering algorithms like K-Means or DBSCAN involved — just smart image analysis and thoughtful engineering.

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
   git clone https://github.com/YOUR_USERNAME/logo-similarity.git
   cd logo-similarity
   ```

2. Create & activate a virtual environment:
   ```bash
   python -m venv logosim_env
   .\logosim_env\Scripts\activate    # Windows
   source logosim_env/bin/activate    # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

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
- [ ] Image processing & similarity logic (in progress)
- [ ] Final grouping output

---

## 🙌 Contributing

Feel free to open issues or submit pull requests if you'd like to help improve or extend this project!

---

## 📃 License

This project is developed for educational purposes as part of the Veridion Internship Challenge.


