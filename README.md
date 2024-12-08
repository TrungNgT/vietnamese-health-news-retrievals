# VIETNAMESE HEALTH NEWS RETRIEVALS
<br>

## 0 . Install requirements:
pip install -r requirements.txt

## 1. Serving Qwen API with vLLM, Openai API and ngrok
- Open and run flowing the Colab notebook: [vllm-serving](https://colab.research.google.com/drive/1k7CoJ-pxoizaGVsXZfkV7SScPOnj2etY?usp=sharing)
- Remember to get the ngrok public URL at the last cell output.
- Adding the URL to the file...

## 2. Serving Elasticsearch cluster on localhost:9200
- You can use your own local elasticsearch module, or the [elasticsearch_analysis_vietnamsese](https://github.com/duydo/elasticsearch-analysis-vietnamese) version.
- Index the documents in the [news](news) folder to the Elasticsearch.

## 3. Run the 