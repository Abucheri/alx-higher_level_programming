#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [...list];

  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    [reversedList[i], reversedList[j]] = [reversedList[j], reversedList[i]];
  }
  return reversedList;
};
