# TypeScript
- 자바스크립트의 타입은 런타임 시점에 확인되는 반면, 타입스크립트의 타입은 컴파일 시점에 확인 됨
⇒ 사전에 확인이 가능하다!
- 타입스크립트는 알아서 타입 추론을 하기 때문에 명시적 선언을 하면 중복이 될 수도 있다..
- object 로 타입을 선언하게 되면 값이 있어도 속성을 찾을 수 없다

```tsx
const person: object ={
    name: 'John',
    age: 30
}
console.log(person.name) // 'object' 형식에 'name' 속성이 없습니다.ts(2339)
```

```tsx
const person: { name: string; age: 1 } = {
  name: "John",
  age: 30, //'30' 형식은 '1' 형식에 할당할 수 없습니다.ts(2322)
};
console.log(person.name);

```

```tsx
const person ={
    name: 'John',
    age: 30
}
console.log(person.name) 
// 그냥 typescript가 알아서 추론하게 두는게 제일 낫다..
```

---

튜플

```tsx
const person: {
  name: string;
  age: number;
  role: [number, string];
} = {
  name: "John",
  age: 30,
  role: [2, "author"],
};

person.role.push("admin"); // push는 예외로 가능
person.role[0] = "admin"; // 'string' 형식은 'number' 형식에 할당할 수 없습니다.ts(2322)

erson.role = [0, "admin", "haha"];
/* '[number, string, string]' 형식은 '[number, string]' 형식에 할당할 수 없습니다.
소스에 3개 요소가 있지만, 대상에서 2개만 허용합니다.ts(2322) */
```

열거형

```tsx
enum Role {
  "ADMIN",
  "READ_ONLY",
  "AUTHOR",
}

const person: {
  name: string;
  age: number;
  hobbies: string[];
  role: Role;
} = {
  name: "John",
  age: 30,
  hobbies: ["Sports", "Cooking"],
  role: Role.ADMIN,
};
```

리터럴 타입

```tsx
const person: {
  name: string;
  age: number;
  hobbies: string[];
  role: 'ADMIN' | 'READ_ONLY' | 'AUTHOR'; // 리터럴 타입 + 유니온

} = {
  name: "John",
  age: 30,
  hobbies: ["Sports", "Cooking"],
  role: 'ADMING', //'"ADMING"' 형식은 '"ADMIN" | "READ_ONLY" | "AUTHOR"' 형식에 할당할 수 없습니다. '"ADMIN"'을(를) 의미했나요?ts(2820)
};

```