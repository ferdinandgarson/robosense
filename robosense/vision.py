import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # downloads on first run

def detect(frame, grid):
    h, w = frame.shape[:2]
    n = len(grid)
    labels = []
    for box in model(frame, verbose=False)[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        labels.append(model.names[int(box.cls[0])])
        for r in range(int(y1/h*n), int(y2/h*n) + 1):
            for c in range(int(x1/w*n), int(x2/w*n) + 1):
                if 0 <= r < n and 0 <= c < n:
                    grid[r][c] = 1
    return grid, labels


if __name__ == "__main__":
    img = cv2.imread("test.jpg")
    grid, labels = detect(img, [[0]*20 for _ in range(20)])
    print(labels)