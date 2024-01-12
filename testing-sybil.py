# testing sybil

print("testing sybil")



import os
from sybil import Serie, Sybil


# Load a trained model
# model = Sybil(
#     name_or_path="sybil_ensemble",
#     calibrator_path=r"C:\Sybil\Sybil",)

model = Sybil("sybil_base")
# print(model)

def list_full_file_paths(directory):
    # List to hold all full file paths
    full_file_paths = []

    # Walk through the directory
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Construct the full file path
            full_path = os.path.join(foldername, filename)
            # Add it to the list
            full_file_paths.append(full_path)

    return full_file_paths


# Set the directory you want to start from
target_directory = r"C:\Sybil\ct-data"
dicom_paths = list_full_file_paths(target_directory)

# Load a trained model
# model = Sybil(
#     name_or_path="sybil_ensemble",
#     calibrator_path=r"C:\\Users\\aakas\\Desktop\\sybil\\ensemble_calibrator.p",
# )

# Get risk scores
serie = Serie(dicom_paths)
scores = model.predict([serie])

print(scores)
# Flatten the list of scores
# Flatten the array of scores
import numpy as np
flat_scores = np.array(scores).flatten()

# Print each score with two decimal places
for score in flat_scores:
    print("{:.4f}".format(score))
# # # You can also evaluate by providing labels
# # serie = Serie(dicom_paths, label=1)
# # results = model.evaluate([serie])