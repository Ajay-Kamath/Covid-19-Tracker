from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Patients
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):

    #query to retrieve number of active patients in each state
    maharashtra_active = Patients.objects.filter(state__exact='maharashtra').filter(status__exact='active').count()
    tamilnadu_active = Patients.objects.filter(state__exact='tamil').filter(status__exact='active').count()
    delhi_active = Patients.objects.filter(state__exact='delhi').filter(status__exact='active').count()
    telangana_active = Patients.objects.filter(state__exact='telangana').filter(status__exact='active').count()
    rajasthan_active = Patients.objects.filter(state__exact='rajasthan').filter(status__exact='active').count()
    uttarpradesh_active = Patients.objects.filter(state__exact='uttar').filter(status__exact='active').count()
    andhrapradesh_active = Patients.objects.filter(state__exact='andhra').filter(status__exact='active').count()
    madhyapradesh_active = Patients.objects.filter(state__exact='madhya').filter(status__exact='active').count()
    kerala_active = Patients.objects.filter(state__exact='kerala').filter(status__exact='active').count()
    gujarat_active = Patients.objects.filter(state__exact='gujarat').filter(status__exact='active').count()
    karnataka_active = Patients.objects.filter(state__exact='karnataka').filter(status__exact='active').count()
    haryana_active = Patients.objects.filter(state__exact='haryana').filter(status__exact='active').count()
    jammuandkashmir_active = Patients.objects.filter(state__exact='jammu').filter(status__exact='active').count()
    punjab_active = Patients.objects.filter(state__exact='punjab').filter(status__exact='active').count()
    westbengal_active = Patients.objects.filter(state__exact='west').filter(status__exact='active').count()
    bihar_active = Patients.objects.filter(state__exact='bihar').filter(status__exact='active').count()
    odisha_active = Patients.objects.filter(state__exact='odisha').filter(status__exact='active').count()
    uttarakhand_active = Patients.objects.filter(state__exact='uttarakhand').filter(status__exact='active').count()
    assam_active = Patients.objects.filter(state__exact='assam').filter(status__exact='active').count()
    himachalpradesh_active = Patients.objects.filter(state__exact='himachal').filter(status__exact='active').count()
    chandigarh_active = Patients.objects.filter(state__exact='chandigarh').filter(status__exact='active').count()
    ladakh_active = Patients.objects.filter(state__exact='ladakh').filter(status__exact='active').count()
    jharkhand_active = Patients.objects.filter(state__exact='jharkhand').filter(status__exact='active').count()
    andamanandnicobarislands_active = Patients.objects.filter(state__exact='andaman').filter(status__exact='active').count()
    chhattisgarh_active = Patients.objects.filter(state__exact='chhattisgarh').filter(status__exact='active').count()
    goa_active = Patients.objects.filter(state__exact='goa').filter(status__exact='active').count()
    puducherry_active = Patients.objects.filter(state__exact='puducherry').filter(status__exact='active').count()
    manipur_active = Patients.objects.filter(state__exact='manipur').filter(status__exact='active').count()
    arunachalpradesh_active = Patients.objects.filter(state__exact='arunachal').filter(status__exact='active').count()
    dadraandnagarhaveli_active = Patients.objects.filter(state__exact='dadra').filter(status__exact='active').count()
    mizoram_active = Patients.objects.filter(state__exact='mizoram').filter(status__exact='active').count()
    tripura_active = Patients.objects.filter(state__exact='tripura').filter(status__exact='active').count()
    meghalaya_active = Patients.objects.filter(state__exact='meghalaya').filter(status__exact='active').count()
    nagaland_active = Patients.objects.filter(state__exact='nagaland').filter(status__exact='active').count()
    sikkim_active = Patients.objects.filter(state__exact='sikkim').filter(status__exact='active').count()
    lakshadweep_active = Patients.objects.filter(state__exact='lakshadweep').filter(status__exact='active').count()

    #query to retrieve number of recovered patients in each state
    maharashtra_recovered = Patients.objects.filter(state__exact='maharashtra').filter(status__exact='recovered').count()
    tamilnadu_recovered = Patients.objects.filter(state__exact='tamil').filter(status__exact='recovered').count()
    delhi_recovered = Patients.objects.filter(state__exact='delhi').filter(status__exact='recovered').count()
    telangana_recovered = Patients.objects.filter(state__exact='telangana').filter(status__exact='recovered').count()
    rajasthan_recovered = Patients.objects.filter(state__exact='rajasthan').filter(status__exact='recovered').count()
    uttarpradesh_recovered = Patients.objects.filter(state__exact='uttar').filter(status__exact='recovered').count()
    andhrapradesh_recovered = Patients.objects.filter(state__exact='andhra').filter(status__exact='recovered').count()
    madhyapradesh_recovered = Patients.objects.filter(state__exact='madhya').filter(status__exact='recovered').count()
    kerala_recovered = Patients.objects.filter(state__exact='kerala').filter(status__exact='recovered').count()
    gujarat_recovered = Patients.objects.filter(state__exact='gujarat').filter(status__exact='recovered').count()
    karnataka_recovered = Patients.objects.filter(state__exact='karnataka').filter(status__exact='recovered').count()
    haryana_recovered = Patients.objects.filter(state__exact='haryana').filter(status__exact='recovered').count()
    jammuandkashmir_recovered = Patients.objects.filter(state__exact='jammu').filter(status__exact='recovered').count()
    punjab_recovered = Patients.objects.filter(state__exact='punjab').filter(status__exact='recovered').count()
    westbengal_recovered = Patients.objects.filter(state__exact='west').filter(status__exact='recovered').count()
    bihar_recovered = Patients.objects.filter(state__exact='bihar').filter(status__exact='recovered').count()
    odisha_recovered = Patients.objects.filter(state__exact='odisha').filter(status__exact='recovered').count()
    uttarakhand_recovered = Patients.objects.filter(state__exact='uttarakhand').filter(status__exact='recovered').count()
    assam_recovered = Patients.objects.filter(state__exact='assam').filter(status__exact='recovered').count()
    himachalpradesh_recovered = Patients.objects.filter(state__exact='himachal').filter(status__exact='recovered').count()
    chandigarh_recovered = Patients.objects.filter(state__exact='chandigarh').filter(status__exact='recovered').count()
    ladakh_recovered = Patients.objects.filter(state__exact='ladakh').filter(status__exact='recovered').count()
    jharkhand_recovered = Patients.objects.filter(state__exact='jharkhand').filter(status__exact='recovered').count()
    andamanandnicobarislands_recovered = Patients.objects.filter(state__exact='andaman').filter(status__exact='recovered').count()
    chhattisgarh_recovered = Patients.objects.filter(state__exact='chhattisgarh').filter(status__exact='recovered').count()
    goa_recovered = Patients.objects.filter(state__exact='goa').filter(status__exact='recovered').count()
    puducherry_recovered = Patients.objects.filter(state__exact='puducherry').filter(status__exact='recovered').count()
    manipur_recovered = Patients.objects.filter(state__exact='manipur').filter(status__exact='recovered').count()
    arunachalpradesh_recovered = Patients.objects.filter(state__exact='arunachal').filter(status__exact='recovered').count()
    dadraandnagarhaveli_recovered = Patients.objects.filter(state__exact='dadra').filter(status__exact='recovered').count()
    mizoram_recovered = Patients.objects.filter(state__exact='mizoram').filter(status__exact='recovered').count()
    tripura_recovered = Patients.objects.filter(state__exact='tripura').filter(status__exact='recovered').count()
    meghalaya_recovered = Patients.objects.filter(state__exact='meghalaya').filter(status__exact='recovered').count()
    nagaland_recovered = Patients.objects.filter(state__exact='nagaland').filter(status__exact='recovered').count()
    sikkim_recovered = Patients.objects.filter(state__exact='sikkim').filter(status__exact='recovered').count()
    lakshadweep_recovered = Patients.objects.filter(state__exact='lakshadweep').filter(status__exact='recovered').count()

    #query to retrieve number of deceased patients in each state
    maharashtra_deceased = Patients.objects.filter(state__exact='maharashtra').filter(status__exact='deceased').count()
    tamilnadu_deceased = Patients.objects.filter(state__exact='tamil').filter(status__exact='deceased').count()
    delhi_deceased = Patients.objects.filter(state__exact='delhi').filter(status__exact='deceased').count()
    telangana_deceased = Patients.objects.filter(state__exact='telangana').filter(status__exact='deceased').count()
    rajasthan_deceased = Patients.objects.filter(state__exact='rajasthan').filter(status__exact='deceased').count()
    uttarpradesh_deceased = Patients.objects.filter(state__exact='uttar').filter(status__exact='deceased').count()
    andhrapradesh_deceased = Patients.objects.filter(state__exact='andhra').filter(status__exact='deceased').count()
    madhyapradesh_deceased = Patients.objects.filter(state__exact='madhya').filter(status__exact='deceased').count()
    kerala_deceased = Patients.objects.filter(state__exact='kerala').filter(status__exact='deceased').count()
    gujarat_deceased = Patients.objects.filter(state__exact='gujarat').filter(status__exact='deceased').count()
    karnataka_deceased = Patients.objects.filter(state__exact='karnataka').filter(status__exact='deceased').count()
    haryana_deceased = Patients.objects.filter(state__exact='haryana').filter(status__exact='deceased').count()
    jammuandkashmir_deceased = Patients.objects.filter(state__exact='jammu').filter(status__exact='deceased').count()
    punjab_deceased = Patients.objects.filter(state__exact='punjab').filter(status__exact='deceased').count()
    westbengal_deceased = Patients.objects.filter(state__exact='west').filter(status__exact='deceased').count()
    bihar_deceased = Patients.objects.filter(state__exact='bihar').filter(status__exact='deceased').count()
    odisha_deceased = Patients.objects.filter(state__exact='odisha').filter(status__exact='deceased').count()
    uttarakhand_deceased = Patients.objects.filter(state__exact='uttarakhand').filter(status__exact='deceased').count()
    assam_deceased = Patients.objects.filter(state__exact='assam').filter(status__exact='deceased').count()
    himachalpradesh_deceased = Patients.objects.filter(state__exact='himachal').filter(status__exact='deceased').count()
    chandigarh_deceased = Patients.objects.filter(state__exact='chandigarh').filter(status__exact='deceased').count()
    ladakh_deceased = Patients.objects.filter(state__exact='ladakh').filter(status__exact='deceased').count()
    jharkhand_deceased = Patients.objects.filter(state__exact='jharkhand').filter(status__exact='deceased').count()
    andamanandnicobarislands_deceased = Patients.objects.filter(state__exact='andaman').filter(status__exact='deceased').count()
    chhattisgarh_deceased = Patients.objects.filter(state__exact='chhattisgarh').filter(status__exact='deceased').count()
    goa_deceased = Patients.objects.filter(state__exact='goa').filter(status__exact='deceased').count()
    puducherry_deceased = Patients.objects.filter(state__exact='puducherry').filter(status__exact='deceased').count()
    manipur_deceased = Patients.objects.filter(state__exact='manipur').filter(status__exact='deceased').count()
    arunachalpradesh_deceased = Patients.objects.filter(state__exact='arunachal').filter(status__exact='deceased').count()
    dadraandnagarhaveli_deceased = Patients.objects.filter(state__exact='dadra').filter(status__exact='deceased').count()
    mizoram_deceased = Patients.objects.filter(state__exact='mizoram').filter(status__exact='deceased').count()
    tripura_deceased = Patients.objects.filter(state__exact='tripura').filter(status__exact='deceased').count()
    meghalaya_deceased = Patients.objects.filter(state__exact='meghalaya').filter(status__exact='deceased').count()
    nagaland_deceased = Patients.objects.filter(state__exact='nagaland').filter(status__exact='deceased').count()
    sikkim_deceased = Patients.objects.filter(state__exact='sikkim').filter(status__exact='deceased').count()
    lakshadweep_deceased = Patients.objects.filter(state__exact='lakshadweep').filter(status__exact='deceased').count()


    maharashtra_confirmed = maharashtra_active + maharashtra_recovered + maharashtra_deceased
    tamilnadu_confirmed = tamilnadu_active + tamilnadu_recovered + tamilnadu_deceased
    delhi_confirmed = delhi_active + delhi_recovered + delhi_deceased
    telangana_confirmed = telangana_active + telangana_recovered + telangana_deceased
    rajasthan_confirmed = rajasthan_active + rajasthan_recovered + rajasthan_deceased
    uttarpradesh_confirmed = uttarpradesh_active + uttarpradesh_recovered + uttarpradesh_deceased
    andhrapradesh_confirmed = andhrapradesh_active + andhrapradesh_recovered + andhrapradesh_deceased
    madhyapradesh_confirmed = madhyapradesh_active + madhyapradesh_recovered + madhyapradesh_deceased
    kerala_confirmed = kerala_active + kerala_recovered + kerala_deceased
    gujarat_confirmed = gujarat_active + gujarat_recovered + gujarat_deceased
    karnataka_confirmed = karnataka_active + karnataka_recovered + karnataka_deceased
    haryana_confirmed = haryana_active + haryana_recovered + haryana_deceased
    jammuandkashmir_confirmed = jammuandkashmir_active + jammuandkashmir_recovered + jammuandkashmir_deceased
    punjab_confirmed = punjab_active + punjab_recovered + punjab_deceased
    westbengal_confirmed = westbengal_active + westbengal_recovered + westbengal_deceased
    bihar_confirmed = bihar_active + bihar_recovered + bihar_deceased
    odisha_confirmed = odisha_active + odisha_recovered + odisha_deceased
    uttarakhand_confirmed = uttarakhand_active + uttarakhand_recovered + uttarakhand_deceased
    assam_confirmed = assam_active + assam_recovered + assam_deceased
    himachalpradesh_confirmed = himachalpradesh_active + himachalpradesh_recovered + himachalpradesh_deceased
    chandigarh_confirmed = chandigarh_active + chandigarh_recovered + chandigarh_deceased
    ladakh_confirmed = ladakh_active + ladakh_recovered + ladakh_deceased
    jharkhand_confirmed = jharkhand_active + jharkhand_recovered + jharkhand_deceased
    andamanandnicobarislands_confirmed = andamanandnicobarislands_active + andamanandnicobarislands_recovered + andamanandnicobarislands_deceased
    chhattisgarh_confirmed = chhattisgarh_active + chhattisgarh_recovered + chhattisgarh_deceased
    goa_confirmed = goa_active + goa_recovered + goa_deceased
    puducherry_confirmed = puducherry_active + puducherry_recovered + puducherry_deceased
    manipur_confirmed = manipur_active + manipur_recovered + manipur_deceased
    arunachalpradesh_confirmed = arunachalpradesh_active + arunachalpradesh_recovered + arunachalpradesh_deceased
    dadraandnagarhaveli_confirmed = dadraandnagarhaveli_active + dadraandnagarhaveli_recovered + dadraandnagarhaveli_deceased
    mizoram_confirmed = mizoram_active + mizoram_recovered + mizoram_deceased
    tripura_confirmed = tripura_active + tripura_recovered + tripura_deceased
    meghalaya_confirmed = meghalaya_active + meghalaya_recovered + meghalaya_deceased
    nagaland_confirmed = nagaland_active + nagaland_recovered + nagaland_deceased
    sikkim_confirmed = sikkim_active + sikkim_recovered + sikkim_deceased
    lakshadweep_confirmed = lakshadweep_active + lakshadweep_recovered + lakshadweep_deceased

    return render(request, 'home.html', {'maharashtra_active':maharashtra_active, 'tamilnadu_active':tamilnadu_active, 'delhi_active':delhi_active, 'telangana_active':telangana_active, 'rajasthan_active':rajasthan_active, 'uttarpradesh_active':uttarpradesh_active, 'andhrapradesh_active':andhrapradesh_active, 'madhyapradesh_active':madhyapradesh_active, 'kerala_active':kerala_active, 'gujarat_active':gujarat_active, 'karnataka_active':karnataka_active, 'haryana_active':haryana_active, 'jammuandkashmir_active':jammuandkashmir_active, 'punjab_active':punjab_active, 'westbengal_active':westbengal_active, 'bihar_active':bihar_active, 'odisha_active':odisha_active, 'uttarakhand_active':uttarakhand_active, 'assam_active':assam_active, 'himachalpradesh_active':himachalpradesh_active, 'chandigarh_active':chandigarh_active, 'ladakh_active':ladakh_active, 'jharkhand_active':jharkhand_active, 'andamanandnicobarislands_active':andamanandnicobarislands_active, 'chhattisgarh_active':chhattisgarh_active, 'goa_active':goa_active, 'puducherry_active':puducherry_active, 'manipur_active':manipur_active, 'arunachalpradesh_active':arunachalpradesh_active, 'dadraandnagarhaveli_active':dadraandnagarhaveli_active, 'mizoram_active':mizoram_active, 'tripura_active':tripura_active, 'meghalaya_active':meghalaya_active, 'nagaland_active':nagaland_active, 'sikkim_active':sikkim_active, 'lakshadweep_active':lakshadweep_active,
                                         'maharashtra_recovered':maharashtra_recovered, 'tamilnadu_recovered':tamilnadu_recovered, 'delhi_recovered':delhi_recovered, 'telangana_recovered':telangana_recovered, 'rajasthan_recovered':rajasthan_recovered, 'uttarpradesh_recovered':uttarpradesh_recovered, 'andhrapradesh_recovered':andhrapradesh_recovered, 'madhyapradesh_recovered':madhyapradesh_recovered, 'kerala_recovered':kerala_recovered, 'gujarat_recovered':gujarat_recovered, 'karnataka_recovered':karnataka_recovered, 'haryana_recovered':haryana_recovered, 'jammuandkashmir_recovered':jammuandkashmir_recovered, 'punjab_recovered':punjab_recovered, 'westbengal_recovered':westbengal_recovered, 'bihar_recovered':bihar_recovered, 'odisha_recovered':odisha_recovered, 'uttarakhand_recovered':uttarakhand_recovered, 'assam_recovered':assam_recovered, 'himachalpradesh_recovered':himachalpradesh_recovered, 'chandigarh_recovered':chandigarh_recovered, 'ladakh_recovered':ladakh_recovered, 'jharkhand_recovered':jharkhand_recovered, 'andamanandnicobarislands_recovered':andamanandnicobarislands_recovered, 'chhattisgarh_recovered':chhattisgarh_recovered, 'goa_recovered':goa_recovered, 'puducherry_recovered':puducherry_recovered, 'manipur_recovered':manipur_recovered, 'arunachalpradesh_recovered':arunachalpradesh_recovered, 'dadraandnagarhaveli_recovered':dadraandnagarhaveli_recovered, 'mizoram_recovered':mizoram_recovered, 'tripura_recovered':tripura_recovered, 'meghalaya_recovered':meghalaya_recovered, 'nagaland_recovered':nagaland_recovered, 'sikkim_recovered':sikkim_recovered, 'lakshadweep_recovered':lakshadweep_recovered,
                                         'maharashtra_deceased':maharashtra_deceased, 'tamilnadu_deceased':tamilnadu_deceased, 'delhi_deceased':delhi_deceased, 'telangana_deceased':telangana_deceased, 'rajasthan_deceased':rajasthan_deceased, 'uttarpradesh_deceased':uttarpradesh_deceased, 'andhrapradesh_deceased':andhrapradesh_deceased, 'madhyapradesh_deceased':madhyapradesh_deceased, 'kerala_deceased':kerala_deceased, 'gujarat_deceased':gujarat_deceased, 'karnataka_deceased':karnataka_deceased, 'haryana_deceased':haryana_deceased, 'jammuandkashmir_deceased':jammuandkashmir_deceased, 'punjab_deceased':punjab_deceased, 'westbengal_deceased':westbengal_deceased, 'bihar_deceased':bihar_deceased, 'odisha_deceased':odisha_deceased, 'uttarakhand_deceased':uttarakhand_deceased, 'assam_deceased':assam_deceased, 'himachalpradesh_deceased':himachalpradesh_deceased, 'chandigarh_deceased':chandigarh_deceased, 'ladakh_deceased':ladakh_deceased, 'jharkhand_deceased':jharkhand_deceased, 'andamanandnicobarislands_deceased':andamanandnicobarislands_deceased, 'chhattisgarh_deceased':chhattisgarh_deceased, 'goa_deceased':goa_deceased, 'puducherry_deceased':puducherry_deceased, 'manipur_deceased':manipur_deceased, 'arunachalpradesh_deceased':arunachalpradesh_deceased, 'dadraandnagarhaveli_deceased':dadraandnagarhaveli_deceased, 'mizoram_deceased':mizoram_deceased, 'tripura_deceased':tripura_deceased, 'meghalaya_deceased':meghalaya_deceased, 'nagaland_deceased':nagaland_deceased, 'sikkim_deceased':sikkim_deceased, 'lakshadweep_deceased':lakshadweep_deceased,
                                         'maharashtra_confirmed':maharashtra_confirmed, 'tamilnadu_confirmed':tamilnadu_confirmed, 'delhi_confirmed':delhi_confirmed, 'telangana_confirmed':telangana_confirmed, 'rajasthan_confirmed':rajasthan_confirmed, 'uttarpradesh_confirmed':uttarpradesh_confirmed, 'andhrapradesh_confirmed':andhrapradesh_confirmed, 'madhyapradesh_confirmed':madhyapradesh_confirmed, 'kerala_confirmed':kerala_confirmed, 'gujarat_confirmed':gujarat_confirmed, 'karnataka_confirmed':karnataka_confirmed, 'haryana_confirmed':haryana_confirmed, 'jammuandkashmir_confirmed':jammuandkashmir_confirmed, 'punjab_confirmed':punjab_confirmed, 'westbengal_confirmed':westbengal_confirmed, 'bihar_confirmed':bihar_confirmed, 'odisha_confirmed':odisha_confirmed, 'uttarakhand_confirmed':uttarakhand_confirmed, 'assam_confirmed':assam_confirmed, 'himachalpradesh_confirmed':himachalpradesh_confirmed, 'chandigarh_confirmed':chandigarh_confirmed, 'ladakh_confirmed':ladakh_confirmed, 'jharkhand_confirmed':jharkhand_confirmed, 'andamanandnicobarislands_confirmed':andamanandnicobarislands_confirmed, 'chhattisgarh_confirmed':chhattisgarh_confirmed, 'goa_confirmed':goa_confirmed, 'puducherry_confirmed':puducherry_confirmed, 'manipur_confirmed':manipur_confirmed, 'arunachalpradesh_confirmed':arunachalpradesh_confirmed, 'dadraandnagarhaveli_confirmed':dadraandnagarhaveli_confirmed, 'mizoram_confirmed':mizoram_confirmed, 'tripura_confirmed':tripura_confirmed, 'meghalaya_confirmed':meghalaya_confirmed, 'nagaland_confirmed':nagaland_confirmed, 'sikkim_confirmed':sikkim_confirmed, 'lakshadweep_confirmed':lakshadweep_confirmed})


