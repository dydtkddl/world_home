import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    
def get_plot(x,y,title):
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,5))
    plt.title(title)
    sns.barplot(x=x, y=y )
    plt.xticks(rotation=45)
    # plt.legend(loc='lower right')    
    plt.xlabel('대륙')
    plt.ylabel('연평균 인구10만명당 죽은 사람 수')
    plt.tight_layout()
    
    graph = get_graph()
    return graph
