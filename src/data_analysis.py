def load_data(file_path):
    """Load data from a given file path."""
    import pandas as pd
    return pd.read_csv(file_path)


def analyze_data(data):
    """Perform basic analysis on the data."""
    summary = data.describe()
    return summary


def save_results(results, output_path):
    """Save the analysis results to a given output path."""
    results.to_csv(output_path, index=False)