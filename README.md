
# News Article Summarization Script

This Python script allows you to perform extractive summarization on a set of news articles provided in a CSV file. The script processes the text data, extracts important sentences, and generates a summary for each article.

## Prerequisites

Before running the script, make sure you have the necessary Python libraries installed. You can install them using `pip`:

```bash
pip install nltk pandas
```

## How to Use

1. **Prepare Your CSV File:**

   - Ensure that your CSV file has a column containing the text of the news articles you want to summarize.
   - By default, the script expects this column to be named `article_text`.
   - If your column has a different name, you'll need to modify the script accordingly.

2. **Run the Script:**

   - Run the script using a Python interpreter.
   - The script will prompt you to enter the path to your CSV file.
   - The script will attempt to read the file using different encodings. If successful, it will process the articles and generate summaries.

3. **Modify Column Name:**

   - After uploading your CSV file, **make sure to change the column name** in the script if your text column has a different name. You can find this line in the script:

     ```python
     df['article_text'].tolist()
     ```

   - Replace `'article_text'` with the name of the column in your CSV file that contains the article text.

4. **View Results:**

   - The script will print the original article and its generated summary for each article in the CSV file.

## Example Usage

```bash
python summarize_articles.py
```

## Handling Encoding Errors

If you encounter a `UnicodeDecodeError` when reading the CSV file, the script is designed to automatically try different encodings (`utf-8`, `latin1`, `windows-1252`). If all attempts fail, the script will raise an error and prompt you to check the file encoding.


