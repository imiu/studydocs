# 5.times { print "Odelay!" }

# print "ololo" unless "restaurant".include? "aura"

# ['toast', 'cheese', 'wine'].each { |food| print food.capitalize }

require 'net/http'
Net::HTTP.start('www.ruby-lang.org', 80) do |http|
  print ( http.get( '/robots.txt' ).body)
end