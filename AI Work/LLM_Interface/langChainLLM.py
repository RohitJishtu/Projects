import langchain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import ChatMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
import logging
import urllib.request
import json
import ssl
import time
from typing import Any, List, Mapping, Optional
import tiktoken

class CustomLLM(LLM):
    max_tokens: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        model:str,
        url: str,
        key: str,
        prompt: str,
        temperature: Optional[int] = 0,
        top_p: Optional[float] = 0.90,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        # self.allowSelfSignedHttps(True)  # Uncomment this line if needed
        prompt_len = len(prompt)
        prompt_tokens = self.num_tokens_from_string(prompt)

        if model=='GPT':
            data = {
                "messages": [{"role": "system", "content": prompt}],
                "max_tokens": self.max_tokens,
                "temperature": temperature,
                "top_p": top_p
            }  
            headers = {'Content-Type': 'application/json', 'api-key': key}  # for GPT 

        else:
            data = {
            "input_data": {
            "input_string": [prompt],
            "parameters": {
                "max_new_tokens": 2048,
                "do_sample": True,
                "return_full_text": False}}}
            headers = {"Authorization": key}

        body = str.encode(json.dumps(data))
        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)
            result = response.read()
            result = json.loads(result)
            if model=='GPT':
                return result.get("choices")[0].get("message").get("content") # for GPT
            else:
                return result
            # 

        except urllib.error.HTTPError as error:
            print(f"The request failed with status code: {error.code}")
            raise

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"max_tokens": self.max_tokens}

    def allowSelfSignedHttps(self, allowed: bool):
        # bypass the server certificate verification on client side
        if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context

    def num_tokens_from_string(self, string: str) -> int:
        """Returns the estimated number of tokens in a text string."""
        encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = len(encoding.encode(string))
        return num_tokens

