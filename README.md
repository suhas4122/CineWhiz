Run this command from the main folder

```
sudo docker run --name redis-stack-server -p 6380:6379 -v ./data/embeddings/:/data redis/redis-stack-server:latest
```

Then run the following command from the main folder

```
streamlit run app.py
```