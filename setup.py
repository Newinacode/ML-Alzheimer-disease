from datasets import load_dataset


dataset = load_dataset("Obscure-Entropy/Alzheimer-MRI")

dataset.save_to_disk("./dataset")

