# 🍎 Mathalathinu kuru ennam 

**Pomegranate Seed Counter** is a computer vision and image-processing project that automatically detects and counts pomegranate seeds from an uploaded image.

The system uses **Python, OpenCV, and image-processing techniques** to identify individual seeds and calculate the total number of seeds in the image.

## 🚀 Features

* 📸 Upload a pomegranate seed image
* 🔍 Automatic seed detection
* 🔢 Automatic seed counting
* 🖼️ Display the processed image
* 📊 Show the total number of detected seeds
* 🌐 Simple and user-friendly web interface
* 💾 Store counting results using a database
* ⚡ Fast image processing

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Computer Vision

* OpenCV
* NumPy
* Image Segmentation
* Thresholding
* Morphological Operations
* Contour Detection
* Watershed Algorithm

### Database

* SQLite / MySQL
* SQL

## 🔄 How It Works

```text
Upload Image
     ↓
Image Preprocessing
     ↓
Color / HSV Segmentation
     ↓
Noise Removal
     ↓
Seed Separation
     ↓
Contour Detection
     ↓
Seed Counting
     ↓
Display Result
```

## 📂 Project Structure

```text
pomegranate-seed-counter/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│
├── database/
│   └── database.db
│
└── results/
    └── processed_images/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pomegranate-seed-counter.git
```

### 2. Open the project

```bash
cd pomegranate-seed-counter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python app.py
```

Then open the URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## 📸 Usage

1. Open the web application.
2. Click **Upload Image**.
3. Select a pomegranate seed image.
4. Click **Count Seeds**.
5. The system processes the image.
6. The detected seeds are highlighted.
7. The total seed count is displayed.

## 🧠 Image Processing

The system performs several image-processing steps:

### 1. Preprocessing

The uploaded image is resized and prepared for processing.

### 2. Segmentation

Color-based segmentation is used to separate the pomegranate seeds from the background.

### 3. Noise Removal

Morphological operations remove small unwanted regions and noise.

### 4. Seed Separation

The **distance transform and watershed algorithm** can be used to separate seeds that are touching each other.

### 5. Counting

Individual detected seed regions are identified and counted.

## ⚠️ Accuracy

Counting accuracy can depend on:

* Image quality
* Lighting conditions
* Background color
* Seed color
* Seeds touching or overlapping
* Camera angle
* Image resolution

For better results, use a **clear image with good lighting and a plain contrasting background**.

## 🔮 Future Improvements

* 🤖 Deep-learning-based seed detection
* 📱 Mobile application
* 📈 Counting history and statistics
* ☁️ Cloud-based image processing
* 🎯 Improved detection for overlapping seeds
* 🧠 Machine-learning-based classification
* 📊 Accuracy comparison with manual counting

## 🎯 Applications

* Agricultural research
* Food processing
* Fruit quality analysis
* Educational computer-vision projects
* Automated seed analysis
* Image-processing research

## 👩‍💻 Author

**Krishna Priya UP**

B.Tech Computer Science and Engineering

## 📜 License

This project is created for educational and academic purposes.
