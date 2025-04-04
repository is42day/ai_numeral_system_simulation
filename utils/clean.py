from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import regexp_replace, trim, col

# ------------------------------------------
# 🔹 Whitespace & Spacing
#🧼 PySpark Regex Cheat Sheet for Data Cleaning
#🔹 Whitespace & Spacing
#Regex	Purpose	Example
#\\s+	Match one or more whitespace	" a \t b " → "a b"
#^\\s+	Match leading whitespace	" abc" → "abc"
#\\s+$	Match trailing whitespace	"abc " → "abc"
#`^\s+	\s+$`	Match leading or trailing whitespace
#[^\\S\\r\\n]+	Match inline whitespace (but preserve \n)	"a b" → "a b"
# ------------------------------------------

def remove_all_whitespace(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(trim(col(colname)), r"\s+", ""))

def collapse_multiple_spaces(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(trim(col(colname)), r"\s{2,}", " "))

def trim_leading_trailing(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, trim(col(colname)))

def normalize_whitespace(df: DataFrame, colname: str) -> DataFrame:
    """Preserve one space between words, trim outer whitespace"""
    return df.withColumn(colname, trim(regexp_replace(col(colname), r"\s+", " ")))

# ------------------------------------------
# 🔹 Digits & Numbers
# ------------------------------------------

def keep_only_digits(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^\d]", ""))

def extract_4_digit_year(df: DataFrame, colname: str, new_col: str) -> DataFrame:
    return df.withColumn(new_col, regexp_replace(col(colname), r"(\d{4})", "$1"))

# ------------------------------------------
# 🔹 Letters and Words
# ------------------------------------------

def remove_non_letters(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^A-Za-z]", ""))

def keep_letters_only(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^A-Za-z]", ""))

# ------------------------------------------
# 🔹 Alphanumeric Cleanup
# ------------------------------------------

def remove_non_alphanumeric(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^A-Za-z0-9]", ""))

def keep_alphanumeric_underscore(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^\w]", ""))

# ------------------------------------------
# 🔹 Symbols & Special Characters
# ------------------------------------------

def remove_symbols(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[!@#\$%\^&\*]+", ""))

def remove_non_word_space(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^\w\s]", ""))

# ------------------------------------------
# 🔹 Line Breaks & Control Characters
# ------------------------------------------

def remove_newlines_tabs(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[\r\n\t]+", " "))

def remove_non_ascii(df: DataFrame, colname: str) -> DataFrame:
    return df.withColumn(colname, regexp_replace(col(colname), r"[^\x00-\x7F]", ""))

# ------------------------------------------
# 🔹 General Cleaning
# ------------------------------------------

def full_clean(df: DataFrame, colname: str) -> DataFrame:
    """
    Combines: trim, normalize whitespace, remove non-ASCII, remove punctuation
    """
    return df.withColumn(
        colname,
        regexp_replace(
            trim(regexp_replace(col(colname), r"[^\x00-\x7F]", "")),
            r"[^A-Za-z0-9\s]",
            ""
        )
    )


### example usage

# df = clean.remove_all_whitespace(df, "contract_id")
# df = clean.keep_only_digits(df, "postal_code")
# df = clean.remove_non_ascii(df, "customer_name")
# df = clean.full_clean(df, "notes")

