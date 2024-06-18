# Connection Pool, HikariCP
- Connection
    - JDBC API를 사용해서 DB와 상호작용을 하기 위해서는 Connection 객체 생성이 필요 (DataSource)
    - 그러나 매번 Connection을 생성하는 것은 비용이 많이 들고 비효율적임
- Conneciton Pool
    - 어플리케이션 생성 시점에 미리 Connection 객체를 생성해 둔 상태에서
    DB 요청이 올 때 Connection 객체를 전달하는 방식
    - 매 요청마다 Connection 객체를 생성하지 않아도 됨
    - DB 사용 후에는 Connection 객체를 Pool에 반납하여 재사용
- HikariCP
    - Spring Boot에 기본 내장되어있는 Connection Pooling Framework
    - Connection Pool을 제공하는 DataSource 구현체