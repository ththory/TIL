# H2 Database
- 자바로 작성된 RDBMS로 설치가 필요 없는 인메모리 Database
- 로컬이나 테스트 환경에서 주로 사용 된다 (애플리케이션 실행 마다 초기화)
- Application 실행 시 초기 테이블을 생성하는 방법
    - src/main/resource > schema.sql 생성
        
        ```sql
        # schema.sql
        
        create table book
        (
            id bigint not null,
            title varchar(255) not null,
            author varchar(255) not null,
        
            primary key (id)
        );
        ```
        