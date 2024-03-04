02/13/화

- DNS Server 동작 원리

02/14/수

- 왜 Nodejs를 사용하는가?
  - 비동기I/O 처리 방식을 사용하여 I/O 처리가 많을 때 유용하다
  - CPU 처리가 많은 애플리케이션에는 불리함 -> 차라리 SpringBoot..

02/15/목

- 변수 대입에 대한 어셈블리 언어 (w/chatgpt)

  ```c++
  int main(){
    int x = 10;
  	int y = x;
  }
  ```

  ```assembly
  mov dword ptr [ebp-4], 10  ; 변수 x에 10을 할당. ebp-4는 스택 프레임 내에서 x의 주소를 나타냄.
  mov eax, [ebp-4]  ; 'x'의 값을 eax 레지스터로 로드합니다.
  mov [ebp-8], eax  ; eax 레지스터의 값을 'y'의 주소에 저장합니다.
  ```

- 포인터와 const

  ```c++
  const int a; // int type의 일반 변수인데 이 데이터의 값은 바뀌면 안됨
  const int* a; // int type의 포인터 변수인데 이 데이터 값은 바뀌면 안됨 
  int* const a; // int type의 포인터 변수인데 이 주소 값은 바뀌면 안됨
  const int* const a; // int type의 포인터 변수인데 이 데이터와 주소값은 바뀌면 안됨
  ```

  
