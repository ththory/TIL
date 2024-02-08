02/08/목

- TypeORM whitelist
- Nestjs API 동작 과정
  - Request -> Validation Pipe (DTO 검증) -> Controller -> Service -> Repository (Entity 검증) ->  DB
- Nestjs에서 Repository를 이용할 때, save에 직접 객체를 넣지 않고 Entity로 감싸는 이유?
  - Entity에 검증 로직 (validation)을 넣으면 DTO 뿐만아니라 Entity 단에서도 데이터 검증이 가능함
  - Entity에 Hook을 걸어서 DB 작업 이후 특정 로직을 수행할 수 있게 가능함

