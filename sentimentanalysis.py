import tkinter as tk
import boto3
root = tk.Tk()
# root.geomatery("400 * 240")
root.geometry("400x240")
root.title("Sentimental analysis")

# height of the window
text_example = tk.Text(root,height=12)  
text_example.pack()
def getText():
    aws_mag_con = boto3.session.Session(profile_name='demo_user')
    client = aws_mag_con.client(service_name='comprehend',region_name='us-east-1')
    result = text_example.get('1.0','end')
    print(result)
    response = client.detect_sentiment(Text=result,LanguageCode='en')
    print(response['Sentiment'])
    print(response['SentimentScore'])

btnread = tk.Button(root,height=1,width=10,text="read",command=getText)
btnread.pack()
root.mainloop()