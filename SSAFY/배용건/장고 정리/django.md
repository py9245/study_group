가상환경만들기
python -m venv venv

가상환경 실행
source venv/Scripts/activate 
(sou tap v tap S tap a tap)

requirement 
pip install -r (tab 존나 눌러서 정확한 위치 로 설치 )requirements.txt

pip freeze > requirements.txt 

프로젝트 생성

django-admin startproject 프로젝트명 .

앱 생성

python m tab startapp 앱명

서버 실행하기

python m (tab) anage.py makemigrations

python m tab migrate

python m tab runserver

앱 생성을 했으면 

settings.py 에 들어가서 
생성한 app 을 추가한다 

프로젝트 urls.py 에서 
path ()  - 경로 지정을 할수있음
path('admin/', admin.site.urls),
기본 경로에 admin의 주소에  간다 
    path('articles/', include('articles.urls')),
기본경로 articles 의 주소에 포함되면 앱의 urls.py 로 간다 

여기서 앱의 urls.py 를 만들고



프로젝트의 urls 에서 앱의 urls.py 로 보낼려면 
from django.urls import path, include
include  를 포함한다

path('articles/', include('articles.urls')),

include (이 경로로 보낸다)

articles/urls.py 에서 

from django.urls import path
from . import views

얘네를 적고시작한다 
밑에줄은 현재위치에서 import view 하기

path( '경로 이름지정/' views.뷰즈 파일에서 만든 함수 )

그러면 이어서 views,py 에서 해당 함수를 만들고

앱 파일에서 templates/articles/index.html  등 파일을 생성

def 만들 함수(request):
    
    return render(request, '템플릿의 articles/파일명.html')

그리고 html 파일을 만들어서 확인

# pk = 1

pk가 1인 데이터를 가져와

# pk = pk 

url에서 받은 번호(pk)를 이용해서 해당 데이터를 가져와!

# Diary.objects.all()

다이어리의 데이터를 전부 가져오기

# 댓글 역참조 기능 구현할때는

article.comment_set.all()



# MTV 구조의 역할

Model : 데이터베이스 관련 로직 담당
Template : 사용자에게 보여지는 화면 담당
View : HTTP 요청을 받고 필요한 Model 데이터를 가져오거나 저장해 Template 에 넘겨 HTTP response 형태로 반환


Model 의 역할 
: 데이터베이스 관련 로직을 담당하며, 
테이블 구조, 필드 타입, 제약조건을 정의
ORM 을 통해 CRUD 를 처리한다