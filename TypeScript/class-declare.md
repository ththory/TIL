Class 선언

```typescript
Class Person {
	private name: string;
    
    constructor(name) {
        this.name = name
    }
    
    hello(): void {
        console.log(`Hello, I'm {this.name}`)
    }
}

Person ththory = new Person('Kim')
ththory.hello()
```

