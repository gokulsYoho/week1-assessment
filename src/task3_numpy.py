import numpy as np
marks = np.array([
    (80, 75, 90),
    (65, 70, 72),
    (88, 92, 85),
    (70, 68, 74)
])
print("Shape:", marks.shape)
print("Student averages:", np.round(marks.mean(axis=1), 2))
print("Subject averages:", np.round(marks.mean(axis=0), 2))
grace_marks = marks + 5
print("With grace marks:\n", grace_marks)
weights = np.array([0.3, 0.3, 0.4])
weighted = np.dot(marks, weights)
print("Weighted scores:", np.round(weighted, 2))