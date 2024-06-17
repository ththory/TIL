# baseUrl, paths 설정 (tsconfig)

소스에서 경로를 참조할 때 절대 경로와 상대 경로를 사용할 수 있는데

절대 경로의 경우 환경과 사용자마다 경로가 변경될 수 있고

상대 경로의 경우 가독성이 떨어지며 리팩토링이 어려워진다는 단점이 있다.

```json
"baseUrl": "./", // 최상위 경로 지정
"paths": {
    "@/*": ["src/*"] // 경로 별칭 지정
},  
```

위와 같이 설정하면

@controller/periodController 를 했을 때

 src/controller/periodController 경로에 매핑된다.