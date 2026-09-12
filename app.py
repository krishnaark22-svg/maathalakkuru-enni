from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def count_seeds(image_path):

    image = cv2.imread(image_path)

    # Resize image
    image = cv2.resize(image, (800, 600))

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Pomegranate seed color range
    lower = np.array([0, 50, 40])
    upper = np.array([180, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore very small objects
        if 100 < area < 5000:

            count += 1

            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle around detected seed
            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Display seed number
            cv2.putText(
                image,
                str(count),
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                1
            )

    output_path = os.path.join(
        PROCESSED_FOLDER,
        "result.jpg"
    )

    cv2.imwrite(output_path, image)

    return count, output_path


@app.route("/", methods=["GET", "POST"])
def index():

    count = None
    result_image = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            image_path = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(image_path)

            count, result_image = count_seeds(image_path)

    return render_template(
        "index.html",
        count=count,
        result_image=result_image
    )


if __name__ == "__main__":
    app.run(debug=True)