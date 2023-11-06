# Tien Len Bot API

## Configuration

#### Run locally
- Create conda environment, note that python version should be <span style="color:#9BB8ED;">Python 3.11</span>
```zsh
conda create --name tlmn python=3.11
conda activate tlmn
```

- Install required packages

```zsh
pip install -r requirements.txt --no-cache-dir
```

## Launch the API

- To Launch the API on localhost, run:

```zsh
uvicorn app.main:app --reload   
```

## Example

- Import this [file](TienlenBot.postman_collection.json) to Postman to test API.