# NestJS CLI 사용하기

## 프로젝트 생성

```bash
nest new <project_name>
```

## 모듈 생성

```bash
nest generate module <module_name>

nest generate module messages
# src/messages/messages.module.ts
```

- src 하위에 모듈명으로 디렉토리 생성 및 모듈 파일 생성
(이미 존재하면 해당 dir 내부에 생성)

## 컨트롤러 생성

```bash
nest generate controller <controller_name>

nest generate controller messages
# src/messages/messages.controller.ts
# src/messages/messages.controller.spec.ts
```

- src 하위에 컨트롤러명으로 디렉토리 생성 및 컨트롤러/테스트 파일
(이미 존재하면 해당 dir 내부에 생성)

```bash
nest generate controller mesaages/messages
# src/messages/mesaages/messages.controller.ts
# src/messages/mesaages/messages.controller.spec.ts

nest generate controller messages --flat
# src/messages.controller.ts
# src/messages.controller.spec.ts
```

- controller를 지정하고 싶을 경우 <path>/<controller_name>으로 지정하면 되는데 경로에 하위 디렉토리를 생성하고 싶지 않다면 —flat 옵션을 추가하면 된다.