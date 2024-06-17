# JPA로 Jsonb를 주입하는 방법
- 상황: JPA를 사용하는 중 JSON Type을 DB에 넣어줘야 함
- gradle 의존성 주입
`implementation 'io.hypersistence:hypersistence-utils-hibernate-63:3.7.6'`
    - version은 hibernate version에 맞춰줘야함 ⇒ README 참조
- Entity 내 Type, Column 정의

```
@Type(JsonType.class)
@Column(name = "auth_list", columnDefinition = "jsonb")
private ArrayList<String> authList;
```