# Data ingestion scripts for NSF EAGER grant

Scripts for retrieving, cleaning, and engineering data from multiple repositories.

Intergrated more than 32 million data for grants and publications

Implemented using pyspark scripts in Airflow pipelines for CI/CD

Model implemented for recommendation : Cosine Similarity using TF-IDF


The structure of the repository should be as follows:

```
/nsf_data_ingestion
 /nber
 /arxiv
 /medline
 /grants_gov
```

## How to access the SOS cluster

[Documentation](https://github.com/sciosci/nsf_data_ingestion/wiki/Accessing-and-running-jobs-in-the-SOS-cluster)
