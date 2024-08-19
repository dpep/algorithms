#!/usr/bin/env ruby


def add(x, y)
  size = [x.size, y.size].max
  carray = false

  (0..size).map do |i|
    digit1 = i >= x.size ? false : (x.reverse[i] == '1')
    digit2 = i >= y.size ? false : (y.reverse[i] == '1')

    if digit1 ^ digit2 ^ carray
      carray = digit1 && digit2
      '1'
    else
      carray = digit1 || digit2
      '0'
    end
  end.join.reverse.sub(/^0+(\d)/, '\1')
end

module Binary
  refine String do
    def to_i
      chars.reverse.map.with_index { |c, i| c == '1' ? 2**i : 0 }.sum
    end
  end

  refine Integer do
    def to_s
      left = self
      res = ''

      loop do
        res = (left % 2 == 1 ? '1' : '0') + res
        left = left >> 1

        break res unless left > 0
      end
    end
  end
end


if __FILE__ == $0
  x, y = ARGV[0], ARGV[1]
  res = add(x, y)
  correct = res == (x.to_i(2) + y.to_i(2)).to_s(2)
  puts "#{x} + #{y} => #{res}   (#{correct ? 'correct' : 'wrong!'})"

  using Binary
  puts
  puts "=> #{(x.to_i + y.to_i).to_s}"
end


########  RSpec  ########

require 'rspec'


describe 'add' do
  it { expect(add('0', '0')).to eq '0' }
  it { expect(add('01', '10')).to eq '11' }
  it { expect(add('1', '10')).to eq '11' }
  it { expect(add('101', '1')).to eq '110' }
  it { expect(add('101', '10')).to eq '111' }
  it { expect(add('101', '11')).to eq '1000' }
end


describe Binary do
  using Binary

  describe 'String#to_i' do
    it { expect('1'.to_i).to eq 1 }
    it { expect('10'.to_i).to eq 2 }
    it { expect('11'.to_i).to eq 3 }
    it { expect('100'.to_i).to eq 4 }
    it { expect('101'.to_i).to eq 5 }
  end

  describe 'Integer#to_s' do
    it { expect(1.to_s).to eq '1' }
    it { expect(2.to_s).to eq '10' }
    it { expect(3.to_s).to eq '11' }
    it { expect(4.to_s).to eq '100' }
    it { expect(5.to_s).to eq '101' }
  end
end
