# VIETNAMESE HEALTH NEWS RETRIEVALS
<br>

## 0 . Install requirements:
```bash
pip install -r requirements.txt
```

## 1. Serving Qwen API with vLLM, Openai API and ngrok
- Open and run flowing the Colab notebook: [vllm-serving](https://colab.research.google.com/drive/1k7CoJ-pxoizaGVsXZfkV7SScPOnj2etY?usp=sharing)
- Remember to get the ngrok public URL at the last cell output.
- Adding the URL to the file [req2Qwen](/streamlit-app/req2Qwen.py)

## 2. Serving Elasticsearch cluster on localhost:9200
- You can use your own local elasticsearch module, or the [elasticsearch_analysis_vietnamsese](https://github.com/duydo/elasticsearch-analysis-vietnamese) version.
- Config Elasticsearch CLI with [Client](/elastic-client/Client.py)
- Index the documents in the [news](/news) folder to the Elasticsearch.

## 3. Run the Streamlit App
```bash
cd streamlit-app
streamlit run App.py
```
- Logs of the latest prompt are in the [prompts_log.txt](/prompts_log.txt)

## 4. Basic flow and experiment:

![basic_flow_diagram](basic-flow.png)
<br>
![experiment1](experiment1.gif)
<br>
![experiment2](experiment2.gif)