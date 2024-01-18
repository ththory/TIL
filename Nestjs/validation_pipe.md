# NestJS ValidationPipe

## Validation Check 구성 과정

1. NestJS가 global로 validation 사용할 수 있게 한다.
```javascript
app.useGloblaPipes(
    new ValidationPipe()
)
```
2. check할 DTO 클래스 생성
```javascript
export class CreateMessages {
    content: string;
}
```
3. Validation rule 등록
```javascript
import { IsString } from 'class-validator';

export class CreateMessages {
    // rule 등록
    @IsString()
    content: string;
}
```

4. request handler에 validation 설정하기
```javascript   
    @Post()
    createMessage(@Body() body: CreateMessages){
        ...
    }
```

## Validation Pipe의 동작 과정

- class-transfomer ⇒ json body → DTO Class instance
- class-validator ⇒ DTO의 유효성 체크
- 에러 발생 시, 즉시 리턴됨 /
에러 없을 시, Request Handler의 Body로 전달됨