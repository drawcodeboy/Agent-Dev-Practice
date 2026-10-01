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

#### 이미지 빌드

```bash
docker build -t image-api .
```

- `docker build` -  Dockerfile의 지시대로 이미지를 만든다.
- `-t [image name]:[tag name]` - 이미지 명, 태그 명 지정하여 이미지 만듬. (e.g. `-t image-api:v1`), 태그 명 지정 안 하면 `latest`로 잡힘
- `.` - 현재 폴더를 빌드 컨텍스트로 지정한다. Dockerfile에서 `COPY`로 가져올 파일들의 기준 위치
- Dockerfile의 위치 지정 방법 (지정하지 않으면, `.`에서 탐색하여 씀) : `-f docker/Dockerfile`
    
    ```bash
    docker build -f docker/Dockerfile -t image-api:v1 .
    ```
    
#### Dockerfile 작성

```docker
FROM python:3.12-slim

WORKDIR /app

# CPU용 PyTorch 설치
RUN pip install --no-cache-dir torch torchvision \
    --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- `FROM` - 이미지 가져오기
- `WORKDIR /app` - 이미지 내부 작업 폴더를 `/app`으로 지정한다. `/app`가 없으면 생성한다. 그리고, 이후 명령은 이 위치를 기준으로 실행된다.
- `RUN command` - `command` 명령 실행
- `COPY . .` - 빌드 컨텍스트 모든 파일을 이미지 내부 현재 작업 폴더인 `/app`에 복사한다.
    - `COPY requirements.txt .` - 빌드 컨텍스트 내 `requirements.txt`를 `/app`에 복사한다.
    - `COPY [build context] [target location]`
- `CMD command` - `command` 명령 실행 (단, 컨테이너 시작할 때마다 실행), `RUN command`는 이미지 빌드 중 실행한다. 설치한 패키지나 생성한 파일이 이미지에 저장된다.

#### 컨테이너 실행

```docker
docker run --rm -p 127.0.0.1:8001:8000 image-api
```

- `docker run` - 이미지로 새 컨테이너를 만들고 실행
- `--rm` - 컨테이너가 종료되면 자동으로 삭제한다. 이미지는 남는다.
- `-p 127.0.0.1:8001:8000` - 내 컴퓨터의 `127.0.0.1:8001`으로 들어온 요청을 내부의 `8000`번 포트로 전달한다.
- `image-api` - 실행할 이미지

#### Docker: 이외에 유용한 명령어

- `docker ps` - 돌아가고 있는 docker 컨테이너 프로세스 확인, 닫힌 거까지 확인하려면 `-al` 옵션 붙이면 됨

# Task 6

### To Do

: logging, latency 측정 추가

### Quesitons

#### logging

```python
logger = logging.getLogger("uvicorn.error")
```

- uvicorn이 설정한 로깅 방식으로 그대로 이용하는 로거를 선언

#### app middleware

```python
@app.middleware("http")
```

- HTTP 요청용 미들웨어를 등록
- 미들웨어: 요청이 API에 도달하기 전과 응답이 나가기 전에 실행되는 공통 처리 코드
- 여러 API에 공통으로 필요한 로깅, 인증, 시간 측정 등을 한 곳에서 처리할 수 있음

#### `finally` 문법

- `try`와 `except`에서 하나가 실행 되면, 어느 것이 실행되든 상관 없이 실행 되는 문법

#### `time.perf_counter()`

- 초 단위에 정밀한 시간 체크 함수, `*1000`을 하면 ms 단위로 바뀜

#### `async def` 질문

- `async def`는 본 함수가 처리되는 동안 다른 작업을 허용할 수 있는 비동기 처리 함수의 선언 방법이다.
- 다른 작업을 허용하는 방식은 비동기 처리 함수 내에 `await`를 씀으로서 이를 가능하게 한다.
- 예를 들어, `result = await task_a()`와 같은 라인이 있다고 할 때, `task_a()`가 실행되는 것을 기다리는 동안 이벤트 루프에 등록된 다른 작업을 수행한다. (단, `task_a()`내에서 점유권을 넘기는 코드가 있어야 이벤트 루프에 등록된 다른 작업을 수행할 수 있다.)
    - 이때, 이벤트 루프에 등록된 다른 작업이라고 하는 것은 다음 라인의 코드를 의미하는 것이 아니다. 다음 라인의 코드는 오히려 실행되지 않고 `task_a()`의 실행이 끝날 때까지 기다려야 하는 대상이다.

# Task 7

### To Do

: README 및 API 사용 예제 정리

### Quesitons