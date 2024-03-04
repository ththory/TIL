03/04/월

- explicit: C++ 컴파일러는 생성자를 실행할 때 내재적(암시적)으로 변환 가능한지 확인하게 되는데 이 경우 발생할 수 있는 사이드 이펙트를 방지하기 위해 explicit 로 선언하여 명시적인 호출에서만 사용 가능

  ```c++
  public:
    explicit MyString(int capacity);
  ```

- mutable

  - const 함수는 사용자 관점에서 데이터에 간섭을 주지 않는 함수이다 (불변성)
  - 그러나, 일부 함수에서는 불변한 성격을 가지고 있음에도 외부 변수 사용이 필요한 경우가 있다.
    - Ex) 캐시, 상태 추적, ...
  - 이런 경우 변경이 이루어지는 변수에 대해서 mutable 키워드를 사용해 변경 가능하도록 적용할 수 있다.

  ```c++
  private:
  	mutable Cache cache;
  public:
  	void getData(int num) const {
      cache.update(~~)
    }
  ```

  