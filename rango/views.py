from django.shortcuts import render
from rango.models import Bar
from rango.models import Tapa
from rango.forms import UserForm, UserProfileForm, BarForm, TapaForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#def index(request):
    #return HttpResponse("Rango says hey there world!")	
	
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
	bar_list = Bar.objects.order_by('-visits')[:5]
	tapas_list = Tapa.objects.order_by('-votos')[:5]
	context_dict = {'bares': bar_list, 'tapas': tapas_list}
	

    # Render the response and send it back!
	return render(request, 'rango/index.html', context_dict)
	
def about(request):
	return render(request, 'rango/about.html')
	
def estadisticas(request):
	bar_list = Bar.objects.order_by('-visits')[:5]
	context_dict = {'bares': bar_list}
	return render(request, 'rango/estadisticas.html', context_dict)
	
	
def bar(request, bar_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}

	try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
		bar = Bar.objects.get(slug=bar_name_slug)
		bar.visits = bar.visits + 1
		bar.save()
		context_dict['bar_name'] = bar.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
		tapas = Tapa.objects.filter(bar=bar)

        # Adds our results list to the template context under name pages.
		context_dict['tapas'] = tapas
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
		context_dict['bar'] = bar
	except Bar.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
		pass

    # Go render the response and return it to the client.
	return render(request, 'rango/bar.html', context_dict)
	

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
	registered = False

    # If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
			user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
			profile.save()

            # Update our variable to tell the template registration was successful.
			registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
		else:
			print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

    # Render the template depending on the context.
	return render(request,	'rango/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
			
			
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
		username = request.POST.get('username')
		password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
		if user:
            # Is the account active? It could have been disabled.
			if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/rango/')
			else:
                # An inactive account was used - no logging in!
				return HttpResponse("Your Rango account is disabled.")
		else:
            # Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
	else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
		return render(request, 'rango/login.html', {})
		
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

	
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
	logout(request)

    # Take the user back to the homepage.
	return HttpResponseRedirect('/rango/')
	category
	

def add_bar(request):
    # A HTTP POST?
	if request.method == 'POST':
		form = BarForm(request.POST)

        # Have we been provided with a valid form?
		if form.is_valid():
            # Save the new bar to the database.
			form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
			return index(request)
		else:
            # The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
        # If the request was not a POST, display the form to enter details.
		form = BarForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
	return render(request, 'rango/add_bar.html', {'form': form})
	
def add_tapa(request, bar_name_slug):
	try:
		bar = Bar.objects.get(slug=bar_name_slug)
	except Bar.DoesNotExist:
				bar = None

	if request.method == 'POST':
		form = TapaForm(request.POST)
		if form.is_valid():
			if bar:
				tapa = form.save(commit=False)
				tapa.bar = bar
				tapa.votos = 0
				tapa.save()
                # probably better to use a redirect here.
				return index(request)
		else:
			print form.errors
	else:
		form = TapaForm()

	context_dict = {'form':form, 'bar': bar}

	return render(request, 'rango/add_tapa.html', context_dict)
	
def me_gusta(request, tapa_nombre):
	tapa = Tapa.objects.get(name2=tapa_nombre)
	tapa.votos += 1
	tapa.save()
	return render(request, 'rango/about.html')
	


