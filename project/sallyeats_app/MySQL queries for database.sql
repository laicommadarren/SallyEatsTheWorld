INSERT INTO locations (name, urlname)
VALUES ('Los Angeles', 'losangeles');

INSERT INTO restaurants (name, urlname, yelp_link, image_link, location_id)
VALUES
('Sun Nong Dan', 'sunnongdan_koreatown', 'https://www.yelp.com/biz/sun-nong-dan-los-angeles-5?osq=Sun+Nong+Dan', 'https://s3-media0.fl.yelpcdn.com/bphoto/WHbMIdSuhhOF8Vb8bwEzKg/o.jpg', 1),
('Marugame Monzo', 'marugamemonzo_littletokyo', 'https://www.yelp.com/biz/marugame-monzo-los-angeles-5', 'https://s3-media0.fl.yelpcdn.com/bphoto/lLo1I87ReImHTEVZkHQxkQ/o.jpg', 1),
('Chengdu Taste', 'chengdutaste_alhambra', 'https://www.yelp.com/biz/chengdu-taste-alhambra-6', 'https://s3-media0.fl.yelpcdn.com/bphoto/9bVFWIgb56CTC1rmZzRpoA/o.jpg', 1),
("Porto's Bakery and Cafe", 'portosbakeryandcafe_glendale', 'https://www.yelp.com/biz/portos-bakery-and-cafe-glendale?osq=Porto%27s+Bakery+%26+Cafe', 'https://s3-media0.fl.yelpcdn.com/bphoto/rWq4DJEnW_Mia_RnwjVHYA/o.jpg', 1),
("Golden Deli", 'goldendeli_sangabriel', 'https://www.yelp.com/biz/golden-deli-san-gabriel-san-gabriel-2', 'https://s3-media0.fl.yelpcdn.com/bphoto/XSmW3W0kXzXSCkbUamPhiA/o.jpg', 1);

INSERT INTO dishes (name, description, restaurant_id, image_link)
VALUES
('Galbi Jjim', 'filler description', 1, 'https://s3-media0.fl.yelpcdn.com/bphoto/CoPvRdUjg2JBSAmwUfTS9g/o.jpg'),
('Yang Ji Sulung Tang', 'filler description', 1, 'https://s3-media0.fl.yelpcdn.com/bphoto/xv3YiDE8y-dgVrI70WP3pg/o.jpg'),
('Galbi Tang', 'filler description', 1, 'https://s3-media0.fl.yelpcdn.com/bphoto/zBtO3tfKwMVfT-szaFS44Q/o.jpg'),
('Sea Urchin Udon', 'filler description', 2, 'https://s3-media0.fl.yelpcdn.com/bphoto/bx_4ZtyhwYZ8ZqdVCkE3ww/o.jpg'),
('Mentai Squid Butter Udon', 'filler description', 2, 'https://s3-media0.fl.yelpcdn.com/bphoto/kbHAoUUXoXBTfZ2DrhnivA/o.jpg'),
('Beef Udon', 'filler description', 2, 'https://s3-media0.fl.yelpcdn.com/bphoto/_XhpWWLHJpEWZUAVOrb1Ew/o.jpg'),
('Toothpick Lamb with Cumin', 'filler description', 3, 'https://s3-media0.fl.yelpcdn.com/bphoto/b4j-hoen9juDXtYlWyvMuw/o.jpg'),
('Wonton with Red Chili Sauce', 'filler description', 3, 'https://s3-media0.fl.yelpcdn.com/bphoto/Oh9l7h-f-gTVuqMdBlQnIg/o.jpg'),
('Mung Bean Jelly Noodle with Chili Sauce', 'filler description', 3, 'https://s3-media0.fl.yelpcdn.com/bphoto/9C2wV9fy14dkNl-Duc7uBA/o.jpg'),
('Potato Ball', 'filler description', 4, 'https://s3-media0.fl.yelpcdn.com/bphoto/24CyAim8D6AaQnMG5o_l5Q/o.jpg'),
("Milk'N Berries Cake", 'filler description', 4, 'https://s3-media0.fl.yelpcdn.com/bphoto/66sOCzySFdcoJnBIsd3F4Q/o.jpg'),
('Cheese Roll', 'filler description', 4, 'https://s3-media0.fl.yelpcdn.com/bphoto/48W1wLWe6Gc3E8hY5muOAQ/o.jpg'),
('Phan Cha Gio (Egg Rolls with Vegetables)', 'filler description', 5, 'https://s3-media0.fl.yelpcdn.com/bphoto/c4jDAcFnPLAJpIaaSDcm6w/o.jpg'),
('Pho Dac Biet (Meat Combo with Rice Noodle Soup)', 'filler description', 5, 'https://s3-media0.fl.yelpcdn.com/bphoto/kbSMGASFeM5rkY76BX1osg/o.jpg'),
('Banh Hoi Thit Nuong & Cha Gio (Grilled Pork and Egg Rolls with Thin Rice Vermicelli)', 'filler description', 5, 'https://s3-media0.fl.yelpcdn.com/bphoto/UOCx7_iElWxq1V0jNTI7MQ/o.jpg');

UPDATE dishes SET urlname = 'galbijjim' WHERE id=1;
UPDATE dishes SET urlname = 'yangjisulungtang' WHERE id=2;
UPDATE dishes SET urlname = 'galbitang' WHERE id=3;
UPDATE dishes SET urlname = 'seaurchinudon' WHERE id=4;
UPDATE dishes SET urlname = 'mentaisquidbutterudon' WHERE id=5;
UPDATE dishes SET urlname = 'beefudon' WHERE id=6;
UPDATE dishes SET urlname = 'toothpicklambwithcumin' WHERE id=7;
UPDATE dishes SET urlname = 'wontonwithredchilisauce' WHERE id=8;
UPDATE dishes SET urlname = 'mungbeanjellynoodlewithchilisauce' WHERE id=9;
UPDATE dishes SET urlname = 'potatoball' WHERE id=10;
UPDATE dishes SET urlname = 'milknberriescake' WHERE id=11;
UPDATE dishes SET urlname = 'cheeseroll' WHERE id=12;
UPDATE dishes SET urlname = 'phanchagio' WHERE id=13;
UPDATE dishes SET urlname = 'phodacbiet' WHERE id=14;
UPDATE dishes SET urlname = 'banhoithitnuong_chagio' WHERE id=15;
 
 UPDATE dishes SET description = "Galbi-jjim is a Korean braised short rib dish, commonly made with beef or pork short ribs. Traditionally it was considered to be an expensive dish, served to the wealthy and high-classed. At Sun Nong Dan, they serve exclusively beef dishes. This version is served with a sweet soy seasoning, or with a spicy option. It also comes with carrots, potatoes, and Korean rice cakes. There is an option to add a cheese topping which is torched tableside to create a spectacle." WHERE id = 1;
 UPDATE dishes SET description = "Yang-ji refers to the cut of meat, namely thinly sliced flank, brisket, or plate. Sullungtang is a Korean soup originating from Seoul, the capital of South Korea. It is made from ox bones, often simmer for a few hours at minimum. The fat is skimmed as it cooks for a clean tasting broth. It has a milky appearance, and is commonly served bland with seasoning provided at the table to be added to taste- generally salt, pepper, and green onions. This version is served with thin noodles in the soup." WHERE id = 2;
 UPDATE dishes SET description = "Galbitang is a Korean short rib soup. It is made by simmering beef short ribs with other stewing ingredients, and is a clear soup as fat is skimmed during the cooking process. The short ribs are generally seasoned midway into the cooking process after it has become tender from simmering. Galbitang is commonly served at Korean weddings." WHERE id = 3;