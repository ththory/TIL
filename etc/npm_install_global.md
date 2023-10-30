## npm 전역설치와 지역설치

```shell
npm install ts-node		# 옵션 지정하지 않으면 자동으로 지역설치
npm install -g ts-node	# -g 옵션으로 전역 설치
```

- 지역설치 시 라이브러리를 프로젝트 내 node_modules에 설치
- 전역설치 시 라이브러리를 /usr/local/lib/node_modules에 설치
- ts-node의 경우 시스템에서 명령어 사용이 필요하기 때문에 전역 설치가 필요하다.