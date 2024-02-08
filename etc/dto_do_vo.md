# DTO, DO, VO

세 가지는 객체지향 설계 시에 주로 사용되는 개념이다.

## DTO (Data Transfer Object)

- **사용 사례**: 네트워크를 통해 사용자 정보를 전송하거나, 클라이언트와 서버 간의 통신에 사용합니다.
- **특징**: 데이터 전송에 최적화되어 있으며, 로직을 포함하지 않고 순수한 데이터 구조로만 이루어져 있습니다.
- **예시**: 웹 어플리케이션에서 사용자의 등록 정보를 서버로 전송할 때, `UserDTO`는 사용자 이름, 이메일, 전화번호 등의 필드만을 가지고 있을 수 있습니다. 이 DTO는 데이터베이스에 직접 저장되지 않고 데이터 전송 목적으로만 사용됩니다.

```java
public class UserDTO {
    private String name;
    private String email;
    private String phoneNumber;

    // 여기에는 단순히 데이터를 전달하는 역할만 있기 때문에, 별도의 비즈니스 로직 메서드는 포함하지 않습니다.
}
```

## DO (Domain Object)

- **사용 사례**: 애플리케이션의 비즈니스 로직을 구현하는 데 사용되며, 도메인 모델을 표현합니다.
- **특징**: 비즈니스 로직을 포함할 수 있으며, 데이터베이스의 테이블과 매칭되어 데이터를 영속화하는 데 사용됩니다.
- **예시**: `User` 도메인 객체는 사용자 정보를 나타내지만, 데이터 전송 외에도 사용자의 비즈니스 로직을 처리할 수 있습니다. 예를 들어, 사용자의 나이를 계산하거나, 사용자 권한을 확인하는 메서드를 포함할 수 있습니다.

```java
public class User {
    private String name;
    private String email;
    private Date birthDate;

    public int calculateAge() {
        // 현재 날짜와 birthDate를 비교하여 나이를 계산하는 로직
    }

    // 여기에는 비즈니스 로직을 수행하는 메서드가 추가될 수 있습니다.
}

```

## VO (Value Object)

- **사용 사례**: 불변성을 가진 복합 값들을 표현하는 데 사용됩니다. VO는 동일성이 아닌 동등성에 의해 정의됩니다.
- **특징**: VO는 불변 객체이며, 일단 생성된 후에는 그 상태가 변경되지 않습니다. VO는 자신이 포함하는 값들에 의해 정의됩니다.
- **예시**: `UserName` 값 객체는 사용자의 이름을 표현할 때 사용될 수 있습니다. 이름은 변경될 수 없으며, 같은 이름을 가진 두 `UserName` 객체는 동등하다고 간주됩니다.

```java
public class UserName {
    private final String firstName;
    private final String lastName;

    public UserName(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // 이 객체는 생성된 후에는 변경할 수 없으며, firstName과 lastName에 대한 Getter만 제공됩니다.
}
```