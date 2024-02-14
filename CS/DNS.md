DNS

DNS 서버 동작 순서

### ththory.example.co.kr

1. Local DNS Server (기지국 DNS 서버)
   - 컴퓨터가 LAN선을 통해 인터넷에 최초 연결될 때 해당하는 통신사의 DNS 서버를 로컬 DNS 서버로 등록하게 된다. 이후 사용자가 브라우저에서 도메인 이름을 입력했을 때 Local DNS Server에서 조회를 한다.
   - Local DNS Server에서 조회되지 않는 도메인일 경우 Root DNS Server에 도메인의 IP를 묻는다.
2. Root DNS Server
   - Root DNS Server는 . 주소를 나타낸다
   - Root DNS Server에서 조회되지 않는 도메인일 경우 TLD Server 주소를 찾아 Local DNS Server에게 응답한다. (해당 예제에서는 kr에 해당하는 TLD Server 응답)
3. Top Level Domain Server
   - 최상위 도메인은 도메인네임의 가장 마지막 부분을 말한다.
   - TLD Server에서 조회되지 않는 도메인일 경우 해당 서버에서 찾을 수 있는 TLD Server 주소를 찾아 Local DNS Server에게  응답한다.
   - 서버의 IP 주소를 찾을 때 까지 이 과정을 반복한다.
   - 인터넷 최상위 도메인 (TLD) 서버 목록
   - https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%EB%84%B7_%EC%B5%9C%EC%83%81%EC%9C%84_%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%AA%A9%EB%A1%9D#%EA%B5%AD%EC%A0%9C%ED%99%94_%EC%9D%BC%EB%B0%98_%EC%B5%9C%EC%83%81%EC%9C%84_%EB%8F%84%EB%A9%94%EC%9D%B8
4. Authorities DNS Server
   - 최종 IP 주소를 반환해주는 DNS Server이다
   - 도메인에 해당하는 IP주소를 Local DNS Server로 전달하고 사용자는 Local DNS Server에게 IP 주소를 받아 실제 요청을 전달한다.
5. Caching
   - 도메인-IP주소 쌍은 Local DNS Server에 일정기간 저장되어 동일한 DNS 요청 시 빠르게 응답을 하게 된다.



Q. 도메인 주소에 해당하는 IP를 찾을 수 없다면? (존재하지 않는 도메인명이라면)

A. 도메인을 찾을 수 없다면 TLD Server에서 NXDOMAIN(Non-Existent Domain) 응답을 로컬 DNS 서버로 보낸다.