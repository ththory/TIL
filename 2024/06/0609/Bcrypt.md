# Bcrypt
- Adaptive one way factor란?
    - 의도적으로 해시 시간을 늘려서 암호 확인시간을 늦추므로써 브루트포스를 사용하지 못하도록 함
    - 그 예로 Bcrypt 가 있음
- Bean으로 주입한 순간부터 인증 시에는 비밀번호가 bcrypt로 해시되어 저장소 내 비밀번호와 비교하게 됨.