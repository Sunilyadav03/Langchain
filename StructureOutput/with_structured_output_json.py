from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI()

#Schema
json_schema= {
    "title": "Review",
    "type": "object",
    "properties": {
        "kew_themes": {
            "type": "array",
            "items":{
                "type": "string"
            },
            "description": "write down all the key themes discussed in the review in a list." 
        },
        "summary":{
            "type": "string", 
            "description": "A brief summary of the review"
        },
        "sentiment":{
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return sentiment of the review either negnative, positive or neutral"
        },
        "pros":{
            "type": ["array" ,"null"],
            "items":{
                "type": "string"
            },
            "description": "Write down all the pros inside a list "
        },
        "cons":{
            "type": ["array" ,"null"],
            "items":{
                "type": "string"
            },
            "description": "Write down all the cons inside a list "
        },
        "name":{
            "type": ["string", "null"],
            "description": "Write the name of the reviewer"
        }
    },
    "required":["key_themes", "summary", "sentiment"] 
 }
    

structured_model= model.with_structured_output(json_schema)

result= structured_model.invoke("""I recently upgraded Samsung Galaxy S24 Ultra, and I must say, It's an absolute 
                                powerhouse! The snapdragon 8 Gen 3 processor makes everything lightning fast-whether
                                I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full
                                day even with heavy use, and he 45W fast charging is a lifesaver.
                                
                                The S-pen integeration is a great touch for note-taking and quick sketches, though
                                I don't use it often. what really blew me away is the 200MP camera-the night node 
                                is stunning, capturing crisp, vibrant images even in low light. Zooming upto 100x 
                                actually works well for distant objects, but anything beyond 30x loses quality.
                                
                                However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's
                                One UI still comes with bloatware-why do i need five different Sasung apps for things
                                Google already provides? The $1,300 price tag is also a hard pill to swallow.
                                
                                Pros:
                                Insanely poerfull processor(great for gaming and productivity)
                                Stunning 200MP camera with incredible zoom capabilities
                                Long Battery life with fast charging
                                S-pen is unique and useful
                                
                                Review by Sunil Yadav.
                                """)

print(result)
print(result["summary"])
print(result["sentiment"])
print(result.name)
