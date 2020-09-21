#!/usr/bin/node
exports.esrever = function (list) {
  let j = 0;
  const reverseList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseList[j] = list[i];
    j++;
  }
  return (reverseList);
};
