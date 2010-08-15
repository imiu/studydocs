# plastic_cup = false
# if plastic_cup
#   print "Plastic cup is on the up 'n' up!"
# end
# 
# 
# unless plastic_cup
#   print "Plastic cup is on the down low."
# end
# at_hotel = 1
# print( if at_hotel.nil?
#           "No clue if he's in the hotel." 
#         elsif at_hotel == true
#           "Definitely in." 
#         elsif at_hotel == false
#           "He's out." 
#         else
#           "The system is on the freee-itz." 
#         end )

# print "Type and be diabolical: "
# idea_backwards = gets.reverse
# print idea_backwards


# code_words = {
#   'starmonkeys' => 'Phil and Pete, those prickly chancellors of the New Reich', 
#   'catapult' => 'chucky go-go', 
#   'firebomb' => 'Heat-Assisted Living', 
#   'Nigeria' => "Ny and Jerry's Dry Cleaning (with Donuts)",
#   'Put the kabosh on' => 'Put the cable box on'
# }
# 
# # Get evil idea and swap in code words
# print "Enter your new idea: " 
# idea = gets
# code_words.each do |real, code| 
#   idea.gsub!( real, code )
# end
# 
# # Save the jibberish to a new file
# print "File encoded.  Please enter a name for this idea: " 
# idea_name = gets.strip
# File::open( "idea-" + idea_name + ".txt", "w" ) do |f|
#   f << idea
# end
# 
# 
# # Print each idea out with the words fixed
# Dir['idea-*.txt'].each do |file_name|
#   idea = File.read( file_name )
#   code_words.each do |real, code| 
#     idea.gsub!( code, real )
#   end
#   puts idea
# end


kitty_toys = 
  [:shape => 'sock', :fabrick => 'cashmere'] +
  [:shape => 'mouse', :fabrick => 'calico'] +
  [:shape => 'eggroll', :fabrick => 'chenille']
# Same as
# kitty_toys = [
#   {:shape => 'sock', :fabrick => 'cashmere'},
#   {:shape => 'mouse', :fabrick => 'calico'},
#   {:shape => 'eggroll', :fabrick => 'chenille'}
# ]

# kitty_toys.sort_by { |toy| toy[:shape] }.each do |toy|
#   puts "Blixy has as #{ toy[:shape] } mad of #{ toy[:fabrick] }"
# end

# non_eggroll = 0
# kitty_toys.each do |toy|
#   next if toy[:shape] == 'eggroll'
#   non_eggroll = non_eggroll + 1
# end

kitty_toys.each do |toy|
  break if toy[:fabrick] == 'chenille'
  p toy
end