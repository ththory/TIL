# TypeORM

## TypeScript와 JavaScript를 위한 ORM 라이브러리

### ORM이란?

Object Relational Mapping

어플리케이션과 DB 연결 시 SQL언어가 아닌 어플리케이션 개발 언어로 DB를  접근할 수 있게 해주는 툴

데이터베이스의 레코드를 해당 언어의 객체로 변환해주며, 이 객체들을 사용하여 데이터베이스 CRUD (Create, Read, Update, Delete) 작업을 수행할 수 있게 해줍

- Java - JPA, Hibernate
- Node.js - Squalize, TypeORM

```tsx
const { Entity, PrimaryGeneratedColumn, Column, createConnection } = require("typeorm");

@Entity()
class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column("text")
  name: string;
}

async function main() {
  const connection = await createConnection({
    type: "postgres",
    host: "localhost",
    port: 5432,
    username: "username",
    password: "password",
    database: "database_name",
    entities: [User],
    synchronize: true,
  });

  const userRepository = connection.getRepository(User);

  // 사용자 추가
  const user = new User();
  user.name = "John Doe";
  await userRepository.save(user);

  // 모든 사용자 조회
  const users = await userRepository.find();
  console.log(users);

  // 데이터베이스 연결 종료
  await connection.close();
}

main();
```

장점

- 데이터베이스 구조가 변경되어도 대부분 모델만 수정하면 적용
- 코드가 직관적이고 객체지향적이기 때문에 가독성과 유지보수성이 높음
- 데이터베이스의 종류에 의존하지 않아 쉽게 이동 가능
- 보안 취약점에 강함

단점

- 추상화 계층이 있어 직접 SQL을 사용할 때보다 성능이 저하될 수 있음
- 매우 복잡한 쿼리를 작성하는 것에는 어려움이 있음
- 학습곡선이 있음

### ORM과 비교되는 개념

- Raw SQL (Native SQL)

  - 가장 낮은 수준의 데이터베이스 상호 작용 형태

  ```tsx
  const { Client } = require('pg');
  
  const client = new Client({
    connectionString: 'postgresql://username:password@localhost:5432/database_name'
  });
  
  async function queryDatabase() {
    await client.connect(); // 데이터베이스에 연결
  
    const res = await client.query('SELECT * FROM your_table WHERE condition = $1', ['value']); // Native SQL 쿼리 실행
  
    console.log(res.rows); // 쿼리 결과 출력
  
    await client.end(); // 데이터베이스 연결 종료
  }
  
  queryDatabase();
  ```

  - 장점
    - 추상화 레이어가 없어 빠른 실행 속도 제공
    - 데이터베이스의 모든 기능을 직접 사용할 수 있어 유연성이 높음
    - 데이터베이스와의 상호작용을 제어할 수 있기 때문에 세밀한 최적화와 튜닝 가능
  - 단점
    - 쿼리를 직접 작성하기 때문에 SQL 문법 오류나 오타를 찾기 어려움
    - 복잡한 애플리케이션에서 코드관리 어려워질 수 있음
    - 특정 데이터베이스에 종속되기 때문에 다른 데이터베이스로의 이전 어려움
    - SQL Injection과 같은 보안 이슈에 약함

- QueryBuilder

  - 쿼리의 각 구성 요소(선택, 조인, 조건, 정렬 등)를 개별적인 메소드 호출로 표현

  ```tsx
  const knex = require('knex')({
    client: 'pg',
    connection: {
      host: 'localhost',
      user: 'username',
      password: 'password',
      database: 'database_name'
    }
  });
  
  async function queryDatabase() {
    try {
      const result = await knex('your_table')
        .select('*')
        .where('column_name', 'value')
        .orderBy('id', 'asc');
  
      console.log(result); // 쿼리 결과 출력
    } catch (error) {
      console.error(error);
    } finally {
      await knex.destroy(); // 데이터베이스 연결 종료
    }
  }
  
  queryDatabase();
  ```

  - 장점
    - 쿼리를 단계별로 구성하여 복잡한 쿼리를 이해하기 쉬움
    - 조건에 따라 구성요소를 동적으로 추가 변경 가능
    - SQL injection 공격 방지를 위한 파라미터 바인딩을 자동으로 처리
  - 단점
    - 라이브러리마다의 사용 방법이 있어 QueryBuilder를 사용하기 위한 문법을 학습해야 함
    - QueryBuilder가 자동으로 생성한 SQL이 최적화 되지 않을 수 있음
    - 매우 복잡한 쿼리의 경우 SQL을 직접 작성하는 것보다 가독성이 떨어질 수 있음

### TypeORM 사용법 (CRUD)

```tsx
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  email: string;
}
```

### 데이터베이스 연결

```tsx
import { createConnection } from "typeorm";
import { User } from "./entity/User";

createConnection({
  type: "postgres",
  host: "localhost",
  port: 5432,
  username: "your_username",
  password: "your_password",
  database: "your_database",
  entities: [
    User
  ],
  synchronize: true,
}).then(connection => {
  // 여기에서 CRUD 작업을 시작할 수 있습니다.
}).catch(error => console.log(error));
```

### Create

```tsx
async function createUser() {
  const user = new User();
  user.name = "John Doe";
  user.email = "john.doe@example.com";

  const userRepository = getRepository(User);
  await userRepository.save(user);
}
```

### Read

```tsx
async function findAllUsers() {
  const userRepository = getRepository(User);
  return await userRepository.find();
}
async function findUserByName(name: string) {
  const userRepository = getRepository(User);
  return await userRepository.findOne({ where: { name } });
}
```

### Update

```tsx
async function updateUser(id: number, newName: string, newEmail: string) {
  const userRepository = getRepository(User);
  const user = await userRepository.findOne(id);

  if (user) {
    user.name = newName;
    user.email = newEmail;
    await userRepository.save(user);
  }
}
```

### Delete

```tsx
async function deleteUser(id: number) {
  const userRepository = getRepository(User);
  await userRepository.delete(id);
}
```

### TypeORM의 특징

### **Active Record 및 Data Mapper 패턴 지원**

- Active Record 패턴

  모델 인스턴스 자체에서 데이터베이스 쿼리를 실행

  ```tsx
  import { Entity, PrimaryGeneratedColumn, Column, BaseEntity } from "typeorm";
  
  @Entity()
  export class User extends BaseEntity {
    @PrimaryGeneratedColumn()
    id: number;
  
    @Column()
    name: string;
  
    async saveUser() {
      return await this.save();
    }
  }
  --- Service --
  async function createUser() {
    const user = new User();
    user.name = "John Doe";
    await user.saveUser();
  }
  ```

- Data Mapper 패턴

  모델과 비즈니스 로직을 분리하여 더 유연한 아키텍처를 제공

  ```tsx
  import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";
  
  @Entity()
  export class User {
    @PrimaryGeneratedColumn()
    id: number;
  
    @Column()
    name: string;
  }
  --- Service --
  import { getRepository } from "typeorm";
  import { User } from "./User";
  
  async function createUser() {
    const userRepository = getRepository(User);
  
    const user = new User();
    user.name = "Jane Doe";
    await userRepository.save(user);
  }
  
  async function listUsers() {
    const userRepository = getRepository(User);
    const users = await userRepository.find();
    console.log(users);
  }
  ```

개발자의 선호에 따라 선택하여 개발하면 됨

### **타입스크립트 지원**

### **다양한 데이터베이스 지원**

MySQL, PostgreSQL, MariaDB, SQLite, MS SQL Server, Oracle, WebSQL 등 다양한 SQL 데이터베이스를 지원

### **자동 마이그레이션 생성**

데이터베이스 스키마 변경 시 필요한 마이그레이션을 자동으로 생성할 수 있음

- 마이그레이션?

  **`synchronize`** 옵션을 통해 활성화됩니다. 이 옵션을 **`true`**로 설정하면, 애플리케이션을 시작할 때마다 TypeORM이 엔티티 모델과 데이터베이스 스키마를 비교합니다. 만약 불일치가 발견되면, TypeORM은 데이터베이스 스키마를 엔티티 모델과 일치하도록 자동으로 수정