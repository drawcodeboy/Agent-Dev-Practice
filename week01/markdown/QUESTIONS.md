# Task 1 

### To Do

: FastAPI 기본 문법, GET/POST, Swagger 이해

### Questions

1. HTTP GET이란 무엇인가?
    
    HTTP GET: 클라이언트가 서버로부터 특정한 리소스를 조회하기 위해 사용하는 기본적인 HTTP 요청 메서드
    
    그래서, `app.get(”/”)`은 HTTP GET이 왔을 때, 어떤 함수가 처리할 지 연결하는 데코레이터다.
    
    데코레이터가 붙은 함수가 리턴하는 것을 통해 클라이언트는 데이터를 조회하게 된다. 
    
2. Swagger UI란 무엇인가?
    
    FastAPI가 자동으로 만들어주는 API 테스트용 웹 화면
    
    서버가 http://127.0.0.1:8000이라면 http://127.0.0.1:8000/docs로 접근 가능하다.
    
    역할은 크게 2가지이다.
    
    - 내가 만든 API 목록을 자동으로 문서화
    - 각 API를 브라우저에서 직접 테스트 (Try it out 버튼으로 수행 가능)

# Task 2

### To Do

: 이미지 업로드 API 구현

### Questions

1. `app.post()`는 그럼 해당 URL에 데이터를 보내는 건가?
    
    URL은 네트워크 상에서 특정 자원의 위치를 식별하는 주소다.
    
    그리고, HTTP POST는 특정 URL에 데이터를 보내는 요청이다.
    
    더 나아가 `app.post(”/test”)`는 `/test`라는 URL로 POST 요청이 들어왔을 때, 데코레이트 된 함수를 실행하게 한다.
    
2. 데코레이터에 의해 호출되는 함수 인자들은 항상 type hint를 달아주어야 하는가?
    
    type hint가 필수는 아니지만, 적극적으로 사용하는 것이 정석임. (아직 많이 개발을 해보지 않아서 와닿지 않음. 기능 오류를 내는 것도 아닌 거 같아서)
    
3. `UploadFile`과 `File`은 무엇인가?
    우선, `UploadFile`은 기존 Python 문법에 따르면, type hint로서 역할을 수행한다.

    하지만, FastAPI에서는 역할이 한 가지 더 있는데, `File` 객체가 들어오면 요청 데이터를 `UploadFile`의 객체로 만들어주는 역할도 수행한다. 

    `File(...)`은 HTTP 요청에서 파일을 받겠다는 선언
    `UploadFile`은 받은 파일을 Python에서 다루는 객체 타입

4. `File(...)`에서 `...`을 넣는 건 무슨 문법인가?

    `...`는 파이썬에서 Ellipsis라는 객체 역할을 수행한다. `None` 같은 특수 객체라고 보면 된다.

    더 나아가 `File(...)` 코드를 사용하면 다른 의미가 생긴다. 클라이언트가 `File(...)`가 인자로 쓰인 함수를 요청할 때, 파일을 반드시 보내야 하는 <b>required</b>의 의미가 된다. 왜 이러한 의미가 되는 지는 FastAPI의 구현부를 들여다 보아야 한다. 단순한 탐색으로는 아직 왜 그런지 알아내지 못 했다.

5. `async`는 무엇인가? 함수 앞에 왜 붙이는가?
    
    비동기 처리 함수를 선언하고자 할 때, 붙이는 문법이다. 해당 함수가 실행 될 때, 기다리는 동안 다른 작업을 수행할 수 있도록 한다.

# Task 3

### To Do

: PyTorch pretrained 모델 연결

### Questions

* None

# Task 4

### To Do

: 예외 처리, request/response schema 정리

### Questions

1. `pydantic`의 `BaseModel`을 통해 response의 구조(형태)를 왜 정해두어야 할까? 딕셔너리로 동일한 역할을 수행할 수 있지 않은가?

    * 무엇이 더 나은지 모르겠음.


# Task 5

### To Do

: Dockerfile 작성 및 실행

### Quesitons

# Task 6

### To Do

: logging, latency 측정 추가

### Quesitons

# Task 7

### To Do

: README 및 API 사용 예제 정리

### Quesitons