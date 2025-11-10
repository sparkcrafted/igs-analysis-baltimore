import awswrangler as wr   # pip install awswrangler
import pandas as pd

S3 = "s3://dataeng-landing-wj"
RAW = f"{S3}/raw"
CLEAN = f"{S3}/clean"

def convert_csv_dataset(src_uri: str, dest_uri: str, chunksize: int = 250_000, **read_csv_kwargs):
    """
    Read a large CSV (from S3) in chunks and append to an S3 Parquet dataset.
    """
    it = pd.read_csv(src_uri, chunksize=chunksize, **read_csv_kwargs)
    for i, chunk in enumerate(it, start=1):
        wr.s3.to_parquet(
            df=chunk,
            path=dest_uri,
            dataset=True,
            index=False,
            mode="append"
        )
        print(f"[{dest_uri}] appended chunk {i} rows={len(chunk):,}")

def main():
    # ASEC
    convert_csv_dataset(f"{RAW}/pppub24.csv",         f"{CLEAN}/asec/pppub24/")
    convert_csv_dataset(f"{RAW}/asec_csv_repwgt_2024.csv", f"{CLEAN}/asec/repwgt/")

    # CBP (explicit sep for .txt CSVs)
    convert_csv_dataset(f"{RAW}/cbp23co.txt",      f"{CLEAN}/cbp/23co/",   sep=",", low_memory=False)
    convert_csv_dataset(f"{RAW}/cbp23msa.txt",     f"{CLEAN}/cbp/23msa/",  sep=",", low_memory=False)
    convert_csv_dataset(f"{RAW}/zbp23detail.txt",  f"{CLEAN}/zbp/23detail/", sep=",", low_memory=False)

if __name__ == "__main__":
    main()
