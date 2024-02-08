# Whitelist

Whitelist는 request Body에 포함된 항목 중 정의되지 않은 값을 같이 받을지에 대한 여부를 나타낸다. true 시 정의되지 않는 값은 제외하고 false 시 정의되지 않아도 body로 받는다.

### 예제

DTO

```typescript
import { IsEmail, IsString } from "class-validator";

export class CreateUserDto {
  @IsEmail()
  email: string;
  @IsString()
  password: string;
}

```

requests.http

```http
POST http://localhost:3000/auth/signin
Content-Type: application/json

{
    "email": "example@kt.com",
    "password": "qwerasdf",
    "name": "Kim"
}
```

case 1. whilelist: true

result: { email: 'example@kt.com', password: 'qwerasdf' }

case 2. whitelist: false

Result: { email: 'example@kt.com', password: 'qwerasdf', name: 'Kim' }