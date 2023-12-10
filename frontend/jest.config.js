module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    transform: {
      '^.+\\.(js|jsx|ts|tsx)$': 'ts-jest',
    },
    moduleDirectories: [".yarn/cache", "src"]
  };
  
  