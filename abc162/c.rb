k = gets.to_i
ans = 0
k.times do |a|
  k.times do |b|
    k.times do |c|
      ans += ((a+1).gcd(b+1)).gcd(c+1)
    end
  end
end

puts ans