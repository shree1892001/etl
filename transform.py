import pandas as pd

def apply_transformations(df: pd.DataFrame, transformations: list) -> pd.DataFrame:
    for transformation in transformations:
        transformation_type = transformation["type"]

        if transformation_type == "drop_columns":
            df = df.drop(columns=transformation["columns"])

        elif transformation_type == "filter":
            df = df.query(transformation["condition"])

        elif transformation_type == "rename_columns":
            df = df.rename(columns=transformation["mappings"])

        elif transformation_type == "add_column":
            df[transformation["name"]] = transformation["value"]

        elif transformation_type == "cast_column":
            df[transformation["column"]] = df[transformation["column"]].astype(transformation["data_type"])

        elif transformation_type == "with_column":
            df[transformation["name"]] = eval(transformation["expression"])

        elif transformation_type == "group_by":
            agg_funcs = {col: agg_func for col, agg_func in transformation["aggregations"].items()}
            df = df.groupby(transformation["columns"]).agg(agg_funcs).reset_index()

        elif transformation_type == "order_by":
            df = df.sort_values(by=transformation["columns"], ascending=transformation.get("ascending", True))

        elif transformation_type == "drop_duplicates":
            df = df.drop_duplicates(subset=transformation["subset"])

        elif transformation_type == "limit":
            df = df.head(transformation["count"])

    return df
